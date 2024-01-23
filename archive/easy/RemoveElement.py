import pretty_errors

"""
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        new_nums = []  
        
        for i in nums:
            if i != val:
                new_nums.append(i)
                k += 1
                
        nums[:k] = new_nums
        
        return k

# Create an instance of the Solution class
solution = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2

# Call the isPalindrome method with an integer argument
result = solution.removeElement(nums, val)

# Print the result
print(result)