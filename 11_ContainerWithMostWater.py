def maxArea(height: list[int]) -> int:

    L, R = 0, len(height) - 1
    maxArea = 0

    while L < R:
        area = (R - L) * min(height[R], height[L])
        maxArea = max(maxArea, area)

        if height[L] < height[R]:
            L += 1
        else:
            R -= 1

    return maxArea


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(maxArea([1, 1]))  # 1
print(maxArea([4, 3, 2, 1, 4]))  # 16
