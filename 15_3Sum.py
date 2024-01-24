def threeSum(nums: list[int]) -> list[list[int]]:

    output = set()
    nums = sorted(nums)

    for i in range(len(nums)-2):
        first = nums[i]
        j, k = i + 1, len(nums) - 1

        while j < k:
            second, third = nums[j], nums[k]

            if first + second + third > 0:
                k -= 1
            elif first + second + third < 0:
                j += 1
            else:
                output.add((first, second, third))
                j += 1
                k -= 1

    return output

print(threeSum([-1,0,1,2,-1,-4]))
