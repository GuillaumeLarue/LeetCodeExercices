from binarySearch.main import Solution


class TestBinarySearch:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.search([-1, 0, 3, 5, 9, 12], 9)
        assert self.value == 4

    def test_two(self):
        so = Solution()
        self.value = so.search([-1, 0, 3, 5, 9, 12], 2)
        assert self.value == -1

    def test_three(self):
        so = Solution()
        self.value = so.search([5], 5)
        assert self.value == 0

    def test_four(self):
        so = Solution()
        self.value = so.search([-1,0,5], 0)
        assert self.value == 1

class TestBinarySearch2:
    def test_one(self):
        so = Solution()
        self.value = so.search_2([-1, 0, 3, 5, 9, 12], 9)
        assert self.value == 4

    def test_two(self):
        so = Solution()
        self.value = so.search_2([-1, 0, 3, 5, 9, 12], 2)
        assert self.value == -1

    def test_three(self):
        so = Solution()
        self.value = so.search_2([5], 5)
        assert self.value == 0

    def test_four(self):
        so = Solution()
        self.value = so.search_2([-1,0,5], 0)
        assert self.value == 1