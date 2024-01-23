import pretty_errors

"""

Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among 
the input strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Sort the strings lexicographically to bring potential common prefixes together
        strs.sort()

        first = strs[0]
        last = strs[-1]

        common_prefix = []

        # Iterate through the characters of the first and last strings
        for i, letter in enumerate(first):
            if i < len(last) and first[i] == last[i]:
                common_prefix.append(letter)
            else:
                break

        return "".join(common_prefix)


#strs = ["power", "flow", "flower", "toy"]

#strs = ["flower","flow","flight"]

strs = ["dog","racecar","car"]

#strs = ["a"]

instance = Solution()

solution = instance.longestCommonPrefix(strs=strs)

print(solution)

