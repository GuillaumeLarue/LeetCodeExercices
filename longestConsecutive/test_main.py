from longestConsecutive.main import Solution


class TestLongestConsecutive:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.longestConsecutive([100, 4, 200, 1, 3, 2])
        assert self.value == 4

    def test_two(self):
        so = Solution()
        self.value = so.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        assert self.value == 9

    def test_three(self):
        so = Solution()
        self.value = so.longestConsecutive([1])
        assert self.value == 1

    def test_four(self):
        so = Solution()
        self.value = so.longestConsecutive([])
        assert self.value == 0

    def test_five(self):
        so = Solution()
        self.value = so.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
        assert self.value == 7

    def test_six(self):
        so = Solution()
        self.value = so.longestConsecutive([2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9, 10])
        assert self.value == 9
