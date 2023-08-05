from twoSum.main import Solution


class TestTwoSum:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.twoSum(nums=[2, 7, 11, 15], target=9)
        assert self.value == [0, 1]

    def test_two(self):
        so = Solution()
        self.value = so.twoSum([3, 2, 4], 6)
        assert self.value == [1, 2]

    def test_three(self):
        so = Solution()
        self.value = so.twoSum(nums=[3, 3], target=6)
        assert self.value == [0, 1]
