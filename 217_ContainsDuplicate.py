def containsDuplicate(nums: list[int]) -> bool:
    d = dict()
    for n in nums:
        if not d.get(n):
            d[n] = 1
        else:
            return True
    return False


print(containsDuplicate(nums=[1, 2, 3, 1]))  # True
print(containsDuplicate(nums=[1, 2, 3, 4]))  # False
print(containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
