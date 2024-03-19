from patterns import SlidingWindow, TwoPointers, MergeIntervals
from data_structures import HashTables



if __name__ == "__main__":
    sliding_window_instance = SlidingWindow.SlidingWindowSolutions()
    hash_table_instance = HashTables.HashTableSolutions()
    two_pointers_instance = TwoPointers.TwoPointersSolutions()
    merge_intervals_instance = MergeIntervals.MergeIntervalSolutions()


    """
    Sliding Window
    """
    #ans = sliding_window.findMaxAverage()
    #ans = sliding_window.minSubArrayLen()
    """
    Hash Table
    """
    #ans = hash_table_instance.TwoSum()
    """
    Two Pointers
    """
    #ans = two_pointers_instance.backspaceCompare()
    #ans = two_pointers_instance.IsSubsequence_392()
    ans = two_pointers_instance.MoveZeroes_283()
    """
    Merge Intervals
    """
    #ans = merge_intervals_instance.MergeInterval_56()

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    print(ans)