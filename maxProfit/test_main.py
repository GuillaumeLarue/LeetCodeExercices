from maxProfit.main import Solution


class TestProductExceptSelf:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.maxProfit([7, 1, 5, 3, 6, 4])
        assert self.value == 5

    def test_two(self):
        so = Solution()
        self.value = so.maxProfit([7, 6, 4, 3, 1])
        assert self.value == 0
