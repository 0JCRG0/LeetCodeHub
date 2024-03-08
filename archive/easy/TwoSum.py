import pretty_errors

class Solution:
    def TwoSum(self, target, arr):
        nums = {}
        for i, x in enumerate(arr):
            residual = target - x
            if residual in nums:
                return [nums[residual], i]
            nums[x] = i
        return None


target = 16

arr = [2, 5, 7, 9, 11]

solution = Solution()

ans = solution.TwoSum(target, arr)

print(ans)