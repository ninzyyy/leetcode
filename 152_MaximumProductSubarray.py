def maxProduct(nums: list[int]) -> int:

    result = max(nums)
    currMax, currMin = 1, 1

    for n in nums:
        temp = n * currMax
        currMax = max(n * currMax, n * currMin, n)
        currMin = min(temp, n * currMin, n)
        result = max(result, currMax)

    return result
