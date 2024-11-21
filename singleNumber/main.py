from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        before = 0
        for e in nums:
            before = before ^ e
        return before


if __name__ == '__main__':
    so = Solution()
    print(so.singleNumber([2, 2, 1]) == 1)
