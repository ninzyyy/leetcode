def trap(height: list[int]) -> int:

    L, R = 0, len(height) - 1
    maxL, maxR = height[L], height[R]
    total = 0

    while L < R:

        if maxL < maxR:
            L += 1
            maxL = max(maxL, height[L])
            total += maxL - height[L]

        else:
            R -= 1
            maxR = max(maxR, height[R])
            total += maxR - height[R]

    return total


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))  # 9
