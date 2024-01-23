from typing import List



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        You are given an integer array nums consisting of n elements, and an integer k.

        Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
        Any answer with a calculation error less than 10-5 will be accepted.

        Example 1:

        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
        Example 2:

        Input: nums = [5], k = 1
        Output: 5.00000
        """
        
        n = len(nums)

        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        #Looping the number of times we are sliding the window to the right
        for i in range(0, n - k):

            start = i
            end = i + k

            window_sum = window_sum - nums[start] + nums[end]

            max_avg = max(max_avg, window_sum / k)

        return max_avg



nums = [1,12,-5,-6,50,3]
k = 4

instance = Solution()

result = instance.findMaxAverage(nums=nums, k=k)

print(result)