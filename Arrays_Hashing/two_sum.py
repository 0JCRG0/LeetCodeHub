
def two_sum(arr: list[int]=[2, 5, 7, 11], target: int=16) -> list[int]:
    hash_table = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[num] = i
    return None
