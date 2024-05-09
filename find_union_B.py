def find_union(A, B):
    union_intervals = []
    for interval_a in A:
        if interval_a[0] is None or interval_a[1] is None:
            continue
        for interval_b in B:
            if interval_b[0] is None or interval_b[1] is None:
                continue
            if interval_a[0] > interval_b[0] and interval_a[1] < interval_b[1]:
                union_intervals.append((interval_a, interval_b))
    return union_intervals


def union(A, B):
    result_set = set()

    for extent_a in A:
        for extent_b in B:
            if not extent_a or not extent_b or len(extent_a) != 2 or len(extent_b) != 2:
                continue  # Skip invalid intervals

            # Check for None values and handle them appropriately
            if extent_b[1] is None or extent_a[0] is None:
                continue  # Skip if any endpoint is None
            elif extent_b[1] < extent_a[0]:
                continue  # No overlap, skip to the next pair
            else:
                # There is an overlap, add both intervals to the result set
                result_set.add(extent_a)
                result_set.add(extent_b)

    return sorted(result_set, key=lambda x: (x[0], x[1]))