def threeSum(nums: list[int]) -> list[list[int]]:

    res = []
    nums = sorted(nums)

    for i, val in enumerate(nums):

        # Condition to skip duplicate values in sorted nums
        if i > 0 and val == nums[i - 1]:
            continue

        L, R = i + 1, len(nums) - 1
        while L < R:
            if val + nums[L] + nums[R] < 0:
                L += 1
            elif val + nums[L] + nums[R] > 0:
                R -= 1
            else:
                res.append([nums[i], nums[L], nums[R]])
                L += 1
                while L < R and nums[L] == nums[L - 1]:
                    L += 1

    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
