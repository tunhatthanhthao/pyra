import time
from openpyxl import Workbook
from connection.mongo_connection import connect_to_mongodb
from find_Extend import find_union_pairs_linear 
from find_Extend import merge_intervals
from find_Extend import print_intervals_without_gaps

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


def print_intervals_without_gaps(intervals):
    output_lines = []
    current_line = []
    for interval in intervals:
        if not current_line or interval[0] <= current_line[-1][1]:
            current_line.append(interval)
        else:
            output_lines.append(current_line)
            current_line = [interval]
    output_lines.append(current_line)
    return output_lines

def print_line(intervals):
    line = []
    for interval in intervals:
        line.append(f"({interval[0]},{interval[1]})")
    return line

def main():
    database_name = input("Enter the name of the MongoDB database: ")
    collection_name = input("Enter the name of the MongoDB collection: ")

    with Timer() as timer:
        # Connect to MongoDB
        database, collection = connect_to_mongodb(database_name, collection_name)
        
        # Read all documents from the MongoDB collection
        documents = collection.find()

        # Extract intervals from each document and flatten the list
        interval_lists = []
        for doc in documents:
            intervals = []
            for key in doc:
                if isinstance(doc[key], list):
                    intervals.extend(doc[key])
            interval_lists.append(intervals)

        # Flatten the list of lists
        intervals = [interval for sublist in interval_lists for interval in sublist]

        # Convert intervals to tuples
        intervals = [tuple(interval) for interval in intervals]

        # Find union pairs and merge intervals
        union_pairs = find_union_pairs_linear(intervals, intervals)
        merged_intervals = merge_intervals(union_pairs)
        output_lines = print_intervals_without_gaps(merged_intervals)
        output_filename = "find_Extend_noSql.xlsx"

        # Print intervals
        for line in output_lines:
            print(*print_line(line))

        
        # Exporting to Excel
        wb = Workbook()
        ws = wb.active
        for line in output_lines:
            ws.append(print_line(line))
        wb.save(output_filename)
        print(f"Output written to {output_filename}")

    print(f"Total running time: {timer.secs:.6f} seconds")


if __name__ == "__main__":
    main()
