def maxArea(height: list[int]) -> int:

    total = []
    for L in range(len(height) - 1):
        for R in range(len(height))[L+1:]:
            water = min(height[L], height[R]) * (R-L)
            total.append(water)
    return max(total)

tank = [1,8,6,2,5,4,8,3,7]
print(maxArea(tank))