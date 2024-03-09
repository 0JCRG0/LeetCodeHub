from typing import List

class SlidingWindowSolutions:
    def findMaxAverage(self, nums: List[int]=[1,12,-5,-6,50,3], k: int=4) -> float:
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
    
    def minSubArrayLen(self, target: int=7, nums: List[int]=[2,3,1,2,4,3]) -> int:
        """
        Given an array of positive integers nums and a positive integer target, return the minimal length of a 
        subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
        Example 1:
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        
        Example 2:
        Input: target = 4, nums = [1,4,4]
        Output: 1
        
        Example 3:
        Input: target = 11, nums = [1,1,1,1,1,1,1,1]
        Output: 0
        
        """

        n = len(nums)

        min_len = float('inf')  # Initialize min_len to positive infinity para comparar

        start = 0
        window_sum = 0

        for end in range(n):
            window_sum += nums[end]
            """
            Esto va haciendo el subarray mas grande hasta que el sum sea mayor o igual a target
            Window sum se hará más pequeño (al quitarle el primer elemento del subarray, esto se hará hasta que window_sum sea mayor a target)
            Mientras que el len minimo ya se guardo, este se actualizara cada vez que window sum sea mayor a target.
            """
            #print(window_sum)

            while window_sum >= target:
                #print(window_sum, target)
                min_len = min(min_len, end - start + 1)
                window_sum -= nums[start]
                start += 1

        # Check if a valid subarray was found
        return int(min_len) if min_len != float('inf') else 0



if __name__ == "__main__":
    sliding_window_instance = SlidingWindowSolutions()
    #ans = instance.findMaxAverage()
    ans = sliding_window_instance.minSubArrayLen()
    print(ans)
