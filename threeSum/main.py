from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if i == j or j == k or i == k:
                        continue
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        b = [nums[i], nums[j], nums[k]]
                        a = sorted(b)
                        if not a in res:
                            res.append(a)
        return res
