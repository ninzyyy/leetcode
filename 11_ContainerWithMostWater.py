
def maxArea(height: list[int]) -> int:

    area = 0
    L, R = 0, len(height) - 1

    while L < R:
        water = min(height[L], height[R]) * (R-L)
        area = max(area, water)

        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return area

tank = [1,8,6,2,5,4,8,3,7]
print(maxArea(tank))