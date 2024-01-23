import pretty_errors

"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3


Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

class Solution():
    def majorityElement(self, nums: list[int]) -> int:
        # Initialize the majority element and count.
        majority = None
        count = 0
        
        # Iterate through the array.
        for num in nums:
            # If count is zero, set the current element as the majority element.
            if count == 0:
                majority = num
                count = 1
            # If the current element is equal to the majority element, increment the count.
            elif num == majority:
                count += 1
            # If the current element is different from the majority element, decrement the count.
            else:
                count -= 1
        
        # At the end of the loop, the majority element will be the result.
        return majority, count


solution = Solution()

nums = [2,2,1,1,1,2,2]

majority, count = solution.majorityElement(nums)

print(majority, count)

