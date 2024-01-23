import pretty_errors
from typing import List

"""
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Initialize a variable to keep track of the position to place the next non-zero element
        non_zero_position = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero
            if nums[i] != 0:
                print(f"nums[i]: {nums[i]} nums[non_zero_position]: {nums[non_zero_position]}")

                # Swap the current element with the element at the non_zero_position
                nums[i], nums[non_zero_position] = nums[non_zero_position], nums[i]
                print(f"nums[i]: {nums[i]} nums[non_zero_position]: {nums[non_zero_position]}")

                
                # Move the non_zero_position to the next position
                non_zero_position += 1
                print(nums)

        
nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

instance = Solution()

result = instance.moveZeroes(nums=nums)