def productExceptSelf(nums: list[int]) -> list[int]:

    solution = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        solution[i] = prefix
        prefix *= nums[i]

    post = 1
    for i in range(len(nums) - 1, -1, -1):
        solution[i] *= post
        post *= nums[i]

    return solution


print(productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
