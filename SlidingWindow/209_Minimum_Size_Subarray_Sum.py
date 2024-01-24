from typing import List

class Solution():
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Given an array of positive integers nums and a positive integer target, return the minimal length of a 
        subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
        Example 2:

        Input: target = 4, nums = [1,4,4]
        Output: 1
        Example 3:

        Input: target = 11, nums = [1,1,1,1,1,1,1,1]
        Output: 0
        
        Example 1:
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        """

        n = len(nums)

        min_len = float('inf')  # Initialize min_len to positive infinity para comparar

        start = 0
        window_sum = 0

        for end in range(n):
            window_sum += nums[end]
            #Esto va haciendo el subarray mas grande hasta que el sum sea mayor o igual a target
            #Window sum se hará más pequeño (al quitarle el primer elemento del subarray, esto se hará hasta que window_sum sea mayor a target)
            # Mientras que el len minimo ya se guardo, este se actualizara cada vez que window sum sea mayor a target.
            print(window_sum)

            while window_sum >= target:
                print(window_sum, target)
                min_len = min(min_len, end - start + 1)
                window_sum -= nums[start]
                start += 1

        # Check if a valid subarray was found
        return min_len if min_len != float('inf') else 0

solution = Solution()

ans = solution.minSubArrayLen(target=7, nums=[2,3,1,2,4,3])

print(ans)