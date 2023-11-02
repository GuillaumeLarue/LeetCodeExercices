from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                res = max(res, prices[i] - min)
        return res
