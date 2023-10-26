from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return [1]

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        # Too long and no stack
        res = []
        for i in range(len(temperatures)):
            j = i + 1
            count = 1
            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                j += 1
                count += 1
            if j >= len(temperatures):
                tmp_res = 0
            else:
                tmp_res = count
            res.append(tmp_res)
        return res
