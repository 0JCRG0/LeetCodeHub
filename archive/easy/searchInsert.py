import pretty_errors

"""
Given a sorted array of distinct integers and a
target value, return the index if the target is found.
If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target == num:
                return i
            else:
                nums.append(target)
                sorted_list = sorted(nums)
                for i, num in enumerate(sorted_list):
                    if target == num:
                        return i



solution = Solution()

nums =[1,3,5,6]
target = 2

response = solution.searchInsert(nums, target)

print(response)