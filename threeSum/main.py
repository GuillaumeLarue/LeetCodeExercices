from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        le = len(nums)
        res = []
        for i in range(le):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = le - 1
            while l < r:
                v = nums[i] + nums[l] + nums[r]
                if v == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
                elif v > 0:
                    r -= 1
                else:
                    l += 1

        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        # Too long
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
