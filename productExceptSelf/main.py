from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0] * l
        sufix = [0] * l
        res = [0] * l
        for i in range(l):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]
        for i in range(l-1, -1, -1):
            if i >= (l - 1):
                sufix[i] = nums[i]
            else:
                sufix[i] = sufix[i + 1] * nums[i]
        for i in range(l):
            if (i - 1) < 0:
                res[i] = sufix[i + 1]
            elif (i + 1) >= l:
                res[i] = prefix[i - 1]
            else:
                res[i] = sufix[i + 1] * prefix[i - 1]

        return res

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        # Division forbidden !
        l = len(nums)
        res = [0] * l
        zero = 0
        for i in range(l):
            if nums[i] == 0:
                zero += 1
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
