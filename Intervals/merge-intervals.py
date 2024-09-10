def merge_intervals(intervals: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        previous = merged[-1]

        if previous[1] >= current[0]:
            merged[-1] = [previous[0], max(previous[1], current[1])]
        else:
            merged.append(current)
    return merged
