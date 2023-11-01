from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Iterative solution
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
