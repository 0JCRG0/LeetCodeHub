import pretty_errors

"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the 
squares of its digits. 

Repeat the process until the number equals 1 (where it will stay), or it 
loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution():
    def isHappy(self, n: int) -> bool:
        seen = set()  # Use a set to keep track of numbers seen to detect cycles
        
        while n != 1 and n not in seen:
            seen.add(n)  # Add the current number to the set
            n_str = str(n)
            n = sum(int(digit) ** 2 for digit in n_str)
        
        return n == 1  # Return True if n is 1, else return False
            
#n = 

instance = Solution()

result = instance.isHappy(n=2)

print(result)