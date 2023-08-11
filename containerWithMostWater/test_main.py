from containerWithMostWater.main import Solution


class TestMaxArea:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        assert self.value == 49

    def test_two(self):
        so = Solution()
        self.value = so.maxArea([1, 1])
        assert self.value == 1

    def test_three(self):
        so = Solution()
        self.value = so.maxArea([2, 2])
        assert self.value == 2
