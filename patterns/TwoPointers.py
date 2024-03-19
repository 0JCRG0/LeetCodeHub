from typing import List

class TwoPointersSolutions():
    def backspaceCompare(self, s: str="ab#c", t:str = "ad#c") -> bool:
        """
        Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty.

        Example 1:
            Input: s = "ab#c", t = "ad#c"
            Output: true
            Explanation: Both s and t become "ac".
        
        Example 2:
            Input: s = "ab##", t = "c#d#"
            Output: true
            Explanation: Both s and t become "".
        
        Example 3:
            Input: s = "a#c", t = "b"
            Output: false
            Explanation: s becomes "c" while t becomes "b".

        Constraints:
            1 <= s.length, t.length <= 200
            s and t only contain lowercase letters and '#' characters.

        Solution:
            Start with result = [] and skip = 0.
            Iterate over the string in reverse: "c", "#", "b", "a".
            See 'c': skip is 0, so result = ['c'].
            See '#': increment skip to 1, result is still ['c'].
            See 'b': skip is 1, so reduce skip to 0 and do not add 'b' to result.
            See 'a': skip is 0, so result = ['a', 'c'].
        """
        def compare(string: str):
            skip = 0
            final_str = []
            for s in reversed(string):
                if s == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    final_str.append(s)
            return final_str
        
        return compare(s) == compare(t)
    def IsSubsequence_392(self, s:str = "aeb", t:str = "abcde"):
        """
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting 
        some (can be none) of the characters without disturbing the relative positions of 
        the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

        Example 1:
        Input: s = "abc", t = "ahbgdc"
        Output: true

        Example 2:
        Input: s = "axc", t = "ahbgdc"
        Output: false

        Constraints:
        0 <= s.length <= 100
        0 <= t.length <= 104
        s and t consist only of lowercase English letters.
        """
        s_index, t_index = 0, 0

        # Loop through both strings until we reach the end of one of them
        while s_index < len(s) and t_index < len(t):
            # If the characters match, move to the next character in s
            if s[s_index] == t[t_index]:
                print(s[s_index], t[t_index])
                s_index += 1
            # Always move to the next character in t
            t_index += 1

        # If we've gone through the entire s, then it's a subsequence
        return s_index == len(s)
    def MoveZeroes_283(self, nums: List[int]=[0,1,0,3,12]):
        """
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Example 1:

        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Example 2:
        Input: nums = [0]
        Output: [0]

        Constraints:

        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1
        """
        non_zero_position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                print(f"BEFORE SWAPPING:\nnums[i]: {nums[i]}, nums[non_zero_position]: {nums[non_zero_position]}, nums: {nums}, non_zero_position: {non_zero_position}\n")
                nums[i], nums[non_zero_position] = nums[non_zero_position], nums[i]
                print(f"AFTER SWAPPING:\nnums[i]: {nums[i]}, nums[non_zero_position]: {nums[non_zero_position]}, nums: {nums}, non_zero_position: {non_zero_position}\n")
                non_zero_position += 1
        print(nums)


if __name__ == "__main__":
    instance = TwoPointersSolutions()
    ans = instance.MoveZeroes_283()
    print(ans)

