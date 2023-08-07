from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
        return []
