from productExceptSelf.main import Solution


class TestProductExceptSelf:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.productExceptSelf(nums=[1, 2, 3, 4])
        assert self.value == [24, 12, 8, 6]

    def test_two(self):
        so = Solution()
        self.value = so.productExceptSelf([-1, 1, 0, -3, 3])
        assert self.value == [0, 0, 9, 0, 0]

    def test_three(self):
        so = Solution()
        self.value = so.productExceptSelf([-1, 1, 0, -3, 3])
        assert self.value == [0, 0, 9, 0, 0]

    def test_four(self):
        so = Solution()
        self.value = so.productExceptSelf([0, 0])
        assert self.value == [0, 0]

    def test_five(self):
        so = Solution()
        self.value = so.productExceptSelf([1, 0])
        assert self.value == [0, 1]
