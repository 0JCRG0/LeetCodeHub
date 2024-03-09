from patterns.SlidingWindow import SlidingWindowSolutions
from data_structures.HashTables import HashTableSolutions



if __name__ == "__main__":
    sliding_window_instance = SlidingWindowSolutions()
    hash_table_instance = HashTableSolutions()

    """
    Sliding Window
    """
    #ans = sliding_window.findMaxAverage()
    #ans = sliding_window.minSubArrayLen()
    """
    Hash Table
    """
    ans = hash_table_instance.TwoSum()

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    print(ans)