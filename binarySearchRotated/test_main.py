from binarySearchRotated.main import Solution


class TestRotatedBinarySearch:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.search([4, 5, 6, 7, 0, 1, 2], 0)
        assert self.value == 4

    def test_two(self):
        so = Solution()
        self.value = so.search([4, 5, 6, 7, 0, 1, 2], 2)
        assert self.value == -1

    def test_three(self):
        so = Solution()
        self.value = so.search([5], 5)
        assert self.value == 0

    def test_four(self):
        so = Solution()
        self.value = so.search([5], 0)
        assert self.value == -1

    def test_five(self):
        so = Solution()
        self.value = so.search([1, 3], 3)
        assert self.value == 1

    def test_six(self):
        so = Solution()
        self.value = so.search([1, 3, 5], 5)
        assert self.value == 2

    def test_seven(self):
        so = Solution()
        self.value = so.search([3, 5, 1], 3)
        assert self.value == 0

    def test_eight(self):
        so = Solution()
        self.value = so.search([5, 1, 3], 3)
        assert self.value == 2

    def test_nine(self):
        so = Solution()
        self.value = so.search([10, 1, 3, 4, 6, 8], 6)
        assert self.value == 4