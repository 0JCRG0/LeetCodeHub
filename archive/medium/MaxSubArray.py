import pretty_errors

"""

Example 2:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            print(f"current_sum_before: {current_sum} ")
            current_sum = max(nums[i], current_sum + nums[i])
            print(f"nums[i]: {nums[i]}. current_sum + nums[i]: {current_sum + nums[i]} ")
            print(f"current_sum: {current_sum}")
            # Update max_sum: track the maximum subarray sum
            max_sum = max(max_sum, current_sum)
            print(f"max_sum: {max_sum}\n")


        # Return the maximum subarray sum
        return max_sum


example_1 = [-2,1,-3,4,-1,2,1,-5,4]

instance = Solution()

result = instance.maxSubArray(example_1)

print(result)
