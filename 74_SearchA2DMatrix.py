
def searchMatrix(matrix: list[list[int]], target: int) -> bool:

    L, R = 0, len(matrix) - 1

    while L <= R:
        M = (L + R) // 2
        if target > matrix[M][-1]:
            L = M + 1
        elif target < matrix[M][0]:
            R = M - 1
        else:
            break

    if not (L <= R):
        return False

    M = (L + R) // 2
    l, r = 0, len(matrix[0]) - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[M][m]:
            l = m + 1
        elif target < matrix[M][m]:
            r = m - 1
        else:
            return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 30
print(searchMatrix(matrix, target))