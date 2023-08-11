from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return [1]

    def maxArea2(self, height: List[int]) -> int:
        # Too long
        l = len(height)
        res = 0
        for i in range(l):
            for j in range(i + 1, l):
                res_tmp = min(height[i], height[j]) * (j - i)
                res = max(res, res_tmp)
        return res
