from kokoEatingBananas.main import Solution


class TestLongestConsecutive:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.minEatingSpeed(piles=[3, 6, 7, 11], h=8)
        assert self.value == 4

    def test_two(self):
        so = Solution()
        self.value = so.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5)
        assert self.value == 30

    def test_three(self):
        so = Solution()
        self.value = so.minEatingSpeed([1], h=2)
        assert self.value == 1

    def test_four(self):
        so = Solution()
        self.value = so.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6)
        assert self.value == 23

    def test_five(self):
        so = Solution()
        self.value = so.minEatingSpeed(piles=[312884470], h=312884469)
        assert self.value == 2

# [30, 11, 23, 4, 20]
# [4, 11, 20, 23, 30]
