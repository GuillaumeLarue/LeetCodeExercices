from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        return res
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
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
    
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        # Division forbidden !
        l = len(nums)
        res = [0] * l
        zero = 0
        for i in range(l):
            if nums[i] == 0:
                zero+=1
        if zero >= 2:
            return res
        elif zero == 1:
            mult = 1
            pos_zero = 0
            for i in range(l):
                if nums[i] == 0:
                    pos_zero = i
                else:
                    mult *= nums[i]
            res[pos_zero] = mult
        else:
            mult = 1
            for i in range(l):
                mult *= nums[i]
            for i in range(l):
                res[i] = int(mult / nums[i])

        return res