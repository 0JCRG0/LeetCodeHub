def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        temp = target - num
        if temp in hashmap:
            return [hashmap[temp], i]
        hashmap[num] = i

print(twoSum([2,7,11,15], 9))


