from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lar = len(matrix[0])
        haut = len(matrix)
        l = 0
        r = lar * haut - 1
        while l < r:
            mid = (r + l) // 2
            a, b = i2mat(lar, haut, mid)
            if matrix[a][b] == target:
                return True
            if target < matrix[a][b]:
                r = mid - 1
            else:
                l = mid + 1
        a, b = i2mat(lar, haut, l)
        if l == r and matrix[a][b] == target:
            return True
        return False


def i2mat(lar, haut, i):
    a = i // lar
    b = i % lar
    return a, b


def mat2i(lar, haut, i, j):
    return i * lar + j


if __name__ == '__main__':
    print(i2mat(4, 3, 7))
    print(mat2i(4, 3, 2, 2))
