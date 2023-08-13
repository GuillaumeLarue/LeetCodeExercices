from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        le = len(height)
        res = 0
        l = 0
        r = le - 1
        while l < r:
            res_tmp = min(height[l], height[r]) * (r - l)
            res = max(res, res_tmp)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


    def maxArea2(self, height: List[int]) -> int:
        # Too long
        l = len(height)
        res = 0
        for i in range(l):
            for j in range(i + 1, l):
                res_tmp = min(height[i], height[j]) * (j - i)
                res = max(res, res_tmp)
        return res
