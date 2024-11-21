from typing import List


class Solution:
    def toBit(self, n: int) -> int:
        mask = ~0 << 1
        res = 0
        while n != 0:
            if ~ (mask | n) == 0:
                res += 1
            n = n >> 1
        return res

    def countBits(self, n: int) -> List[int]:
        res = []
        for e in range(n + 1):
            res.append(self.toBit(e))
        return res


class Solution2:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.countBits(5) == [0, 1, 1, 2, 1, 2])

    so2 = Solution2()
    print(so2.countBits(5) == [0, 1, 1, 2, 1, 2])
