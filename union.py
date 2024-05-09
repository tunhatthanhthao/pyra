def union(A, B):
    result_set = set()

    for extent_a in A:
        for extent_b in B:
            if extent_a is None or extent_b is None:
                continue  # Skip if any interval is None
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
