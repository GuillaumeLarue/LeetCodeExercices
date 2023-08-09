from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        if nums == []:
            return 0
        res_tmp = 1
        res = 1
        for i in range(l - 1):
            if (nums[i] - nums[i + 1]) == -1 or (nums[i] - nums[i + 1]) == 1:
                res_tmp += 1
            elif (nums[i] - nums[i + 1]) == 0:
                res_tmp += 0
            else:
                res_tmp = 1
            res = max(res_tmp, res)
        return res
