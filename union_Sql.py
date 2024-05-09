import time
import mysql.connector
from mysql.connector import Error
from openpyxl import Workbook
from connection.connect_to_mysql import connect_to_mysql
from union import union


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.msecs)


def read_intervals_from_mysql(cursor, table_name, start_col, end_col):
    try:
        cursor.execute(f"SELECT {start_col}, {end_col} FROM {table_name}")
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error reading from {table_name}: {e}")
        return []


def get_table_columns(cursor, table_name):
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = [column[0] for column in cursor.fetchall()]
        return columns
    except Error as e:
        print(f"Error fetching columns for {table_name}: {e}")
        return []


def print_intervals_without_gaps(intervals):
    current_line = []
    output_lines = []
    for interval in intervals:
        if not current_line or interval[0] <= current_line[-1][1]:
            current_line.append(interval)
        else:
            output_lines.append(current_line)
            current_line = [interval]
    output_lines.append(current_line)

    for line in output_lines:
        print_line(line)

    return output_lines


def print_line(intervals):
    output_line = []
    for interval in intervals:
        output_line.append(f"({interval[0]},{interval[1]})")
    print(' '.join(output_line))

    return output_line


def main(host=None, user=None, password=None, database=None):
    # Prompt the user for MySQL connection details if not provided
    if None in (host, user, password, database):
        host = input("Enter MySQL host address: ")
        user = input("Enter MySQL username: ")
        password = input("Enter MySQL password: ")
        database = input("Enter MySQL database name: ")

    try:
        db_connection = connect_to_mysql(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if db_connection.is_connected():
            with Timer() as timer:
                cursor = db_connection.cursor()

                # Read intervals from the consolidated table
                interval_lists = []
                columns = get_table_columns(cursor, 'Data_table')
                valid_columns = [col for col in columns if col != 'id']
                for i in range(0, len(valid_columns), 2):
                    start_col, end_col = valid_columns[i], valid_columns[i + 1]
                    intervals = read_intervals_from_mysql(cursor, 'Data_table', start_col, end_col)
                    interval_lists.append(intervals)

                # Perform union operation
                union_result = interval_lists[0]
                for i in range(1, len(interval_lists)):
                    union_result = union(union_result, interval_lists[i])

                # Print result
                output_lines = print_intervals_without_gaps(union_result)

                # Exporting to Excel
                wb = Workbook()
                ws = wb.active
                for line in output_lines:
                    ws.append(print_line(line))
                wb.save("union_mySql.xlsx")
            print(f"Total running time: {timer.secs:.6f} seconds")

    except Exception as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if db_connection.is_connected():
            db_connection.close()


if __name__ == "__main__":
    # Pass MySQL connection parameters here
    main()
