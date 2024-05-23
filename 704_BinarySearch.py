def search(nums: list[int], target: int) -> int:

    left, right = 0, len(nums) - 1

    while left <= right:

        middle = (left + right) // 2

        if nums[middle] < target:
            left = middle + 1

        elif nums[middle] > target:
            right = middle - 1

        else:
            return middle

    return -1


print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))  # 4
print(search(nums=[-1, 0, 3, 5, 9, 12], target=2))  # -1
print(search(nums=[2, 5], target=5))  # 1
