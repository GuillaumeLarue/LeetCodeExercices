from typing import List


def eatingSpeed(piles, h, k) -> bool:
    i = 0
    # find h
    new_h = 0
    for pile in piles:
        new_h += (pile + k - 1) // k
    return new_h <= h


def eatingSpeed_2(piles, h, k) -> bool:
    i = 0

    while True:
        if piles[i] == 0 and i == len(piles) - 1:
            return True
        if h == 0:
            return False
        if piles[i] == 0:
            i += 1
            h += 1
        else:
            piles[i] -= k
            if piles[i] < 0:
                piles[i] = 0
        h -= 1


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        while left < right - 1:
            mid = (right + left) // 2
            if eatingSpeed(piles, h, mid):
                right = mid
            else:
                left = mid
        return right
