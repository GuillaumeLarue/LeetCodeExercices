from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid_1 = 0
        mid_2 = 0
        min_1 = 0
        min_2 = 0
        nums = []
        con = True
        if (m + n) % 2 == 0:
            mid_2 = int((m + n) / 2)
            mid_1 = int(mid_2 - 1)
        else:
            mid_1 = int(((m + n + 1) / 2) - 1)
            mid_2 = int(mid_1)
        while min_1 <= (mid_2) and min_2 <= (mid_2) and con:
            if min_1 < m and min_2 < n and nums1[min_1] <= nums2[min_2]:
                nums.append(nums1[min_1])
                min_1 += 1
            elif min_1 >= m:
                while min_2 < n:
                    nums.append(nums2[min_2])
                    min_2 += 1
                con = False
            elif min_2 >= n:
                while min_1 < m:
                    nums.append(nums1[min_1])
                    min_1 += 1
                con = False
            else:
                nums.append(nums2[min_2])
                min_2 += 1
        return float((float(nums[mid_1] + nums[mid_2])) / float(2))


"""


"""
