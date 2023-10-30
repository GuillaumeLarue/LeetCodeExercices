from binarySearchMatrix.main import Solution


class TestBinarySearchMatrix:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
        assert self.value

    def test_two(self):
        so = Solution()
        self.value = so.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
        assert not self.value

    def test_three(self):
        so = Solution()
        self.value = so.searchMatrix([[5]], 5)
        assert self.value

    def test_four(self):
        so = Solution()
        self.value = so.searchMatrix([[2]], 0)
        assert not self.value
