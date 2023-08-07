from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        for i in range(l):
            tmp = 1
            for j in range(l):
                if i == j:
                    continue
                tmp *= nums[j]
            res[i] = tmp
        return res