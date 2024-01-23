import pretty_errors

class Solution:
    def two_sum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None


# Create an instance of the Solution class
solution = Solution()

# Call the isPalindrome method with an integer argument
nums=[2, 7, 11, 15]
target= 9

result = solution.two_sum(nums, target)

# Print the result
print(result)