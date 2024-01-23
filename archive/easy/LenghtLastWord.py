"""
Given a string s consisting of words and spaces, return the
length of the last word in the string.

A word is a maximal substring
consisting of non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped_s = s.strip()
        splitted_s = stripped_s.split(" ")
        last_word_index = len(splitted_s) - 1
        last_word_str = ""

        for i, num in enumerate(splitted_s):
            if i == last_word_index:
                last_word_str = num
                return len(last_word_str)


s = "Hello World"
s = "   fly me   to   the moon  "

instance = Solution()

solution = instance.lengthOfLastWord(s)

print(solution)