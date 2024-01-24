import math

def minEatingSpeed(piles: list[int], h: int) -> int:

    L, R = 1, max(piles)
    solution = R

    while L <= R:
        k = (L + R) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        if hours <= h:
            solution = min(solution, k)
            R = k - 1
        else:
            L = k + 1

    return solution

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))
# Answer: 4