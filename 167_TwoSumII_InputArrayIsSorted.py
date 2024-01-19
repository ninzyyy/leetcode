
def twoSum(numbers: list[int], target: int):

    L, R = 0, len(numbers) - 1

    while numbers[R] + numbers[L] != target:

        if numbers[R] + numbers[L] > target:
            R -= 1
        elif numbers[R] + numbers[L] < target:
            L += 1

    return [L+1, R+1]

target = 9
numbers = [2,7,11,15]
print(twoSum(numbers, target))