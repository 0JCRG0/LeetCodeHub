import pretty_errors
"""
Given an integer array nums, return true 
if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false


        counter = 0
        for num in reversed(nums):
            nums.pop()
            if num in nums:
                counter += 1
                print(f"yes {num} {nums}")
            else:
                counter += 0
                print(f"no {num} {nums}")
        if counter >= 1:
            return True
        return False

"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

solution = Solution()

nums = [2,14,18,22,2]
response = solution.containsDuplicate(nums)

print(response)