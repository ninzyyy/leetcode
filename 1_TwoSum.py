def twoSum(self, nums: list[int], target: int) -> list[int]:
    d = dict()
    for index, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], index]
        d[num] = index


print(twoSum(0, [2, 7, 11, 15], 9))  # [0,1]
print(twoSum(0, [3, 2, 4], 6))  # [1,2]
print(twoSum(0, [3, 3], 6))  # [0,1]
