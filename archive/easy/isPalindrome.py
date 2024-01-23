import pretty_errors

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        if x_str == x_str[::-1]:
            return True
        else:
            return False


# Create an instance of the Solution class
solution = Solution()

# Call the isPalindrome method with an integer argument
result = solution.isPalindrome(22222)

# Print the result
print(result)