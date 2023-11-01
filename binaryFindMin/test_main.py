from binaryFindMin.main import Solution


class TestBinaryFindMin:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.findMin([3, 4, 5, 1, 2])
        assert self.value == 1

    def test_two(self):
        so = Solution()
        self.value = so.findMin([4, 5, 6, 7, 0, 1, 2])
        assert self.value == 0

    def test_three(self):
        so = Solution()
        self.value = so.findMin([5])
        assert self.value == 5

    def test_four(self):
        so = Solution()
        self.value = so.findMin([-1, 0, 5])
        assert self.value == -1

    def test_five(self):
        so = Solution()
        self.value = so.findMin([2, 1])
        assert self.value == 1

    def test_six(self):
        so = Solution()
        self.value = so.findMin([3, 1, 2])
        assert self.value == 1

    def test_seven(self):
        so = Solution()
        self.value = so.findMin([2, 3, 1])
        assert self.value == 1

    def test_eight(self):
        so = Solution()
        self.value = so.findMin([5, 1, 2, 3, 4])
        assert self.value == 1
