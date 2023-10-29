from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Recursive solution
        def bin_search(nums: List[int], target: int, l: int, r: int):
            #mid = r - l // 2
            mid = (l + r) // 2

            if l > r:
                return -1
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return bin_search(nums, target, l, mid - 1)
            else:
                return bin_search(nums, target, mid + 1, r)

        return bin_search(nums, target, 0, len(nums) - 1)

    def search_2(self, nums: List[int], target: int) -> int:
        # Iterative solution
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        if l == r and nums[l] == target:
            return l
        return -1
