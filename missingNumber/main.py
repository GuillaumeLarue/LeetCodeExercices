from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tmp = []
        for e in range(len(nums) + 1):
            tmp.append(e)
        return sum(tmp) - sum(nums)


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for e in nums:
            res = res ^ e
        for i in range(len(nums) + 1):
            res = res ^ i
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.missingNumber([3, 0, 1]) == 2)
    print(so.missingNumber([0, 1, 2]) == 3)
    print(so.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)

    so2 = Solution2()
    print(so2.missingNumber([3, 0, 1]) == 2)
    print(so2.missingNumber([0, 1, 2]) == 3)
    print(so2.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)
