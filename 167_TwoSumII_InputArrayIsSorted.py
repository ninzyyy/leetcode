def twoSum(numbers: list[int], target: int):

    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left + 1, right + 1]


print(twoSum(numbers=[2, 7, 11, 15], target=9))  # [1, 2]
print(twoSum(numbers=[2, 3, 4], target=6))  # [1, 3]
