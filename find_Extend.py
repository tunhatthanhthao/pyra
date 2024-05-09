def find_union_pairs_linear(A, B):
    union_pairs = set()
    i, j = 0, 0

    while i < len(A) and j < len(B):
        extent_a = A[i]  # Convert list to tuple
        extent_b = B[j]  # Convert list to tuple

        if not extent_a or not extent_b or len(extent_a) != 2 or len(extent_b) != 2:
            continue  # Skip invalid intervals

        if extent_b[1] < extent_a[0]:
            print(f"{extent_b[1]} < {extent_a[0]}: {extent_b[1] < extent_a[0]}")
            j += 1
        else:
            # There is an overlap, add both intervals to the union pairs set
            union_pairs.add(extent_a)
            union_pairs.add(extent_b)
            i += 1
            j += 1  # Move both pointers forward

    return sorted(union_pairs, key=lambda x: (x[0], x[1]))


def merge_intervals(union_pairs):
    union_pairs = sorted(union_pairs, key=lambda x: (x[0], x[1]))
    merged_intervals = set()

    for i in range(len(union_pairs)):
        for j in range(i + 1, len(union_pairs)):
            # Check if intervals can be merged
            if union_pairs[i][1] >= union_pairs[j][0]:
                merged_intervals.add((union_pairs[i][0], union_pairs[j][1]))

    return sorted(merged_intervals, key=lambda x: (x[0], x[1]))

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

