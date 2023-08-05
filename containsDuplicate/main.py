from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for e in nums:
            if e in s:
                return True
            else:
                s.add(e)
        return False