from lengthOfLongestSubstring.main import Solution


class TestLengthOfLongestSubstring:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.lengthOfLongestSubstring("saf")
        assert self.value == 3

    def test_two(self):
        so = Solution()
        self.value = so.lengthOfLongestSubstring("pwwkew")
        assert self.value == 3

    def test_three(self):
        so = Solution()
        self.value = so.lengthOfLongestSubstring("aabcvr")
        assert self.value == 5

    def test_four(self):
        so = Solution()
        self.value = so.lengthOfLongestSubstring("dvazerdf")
        assert self.value == 7

    def test_five(self):
        so = Solution()
        self.value = so.lengthOfLongestSubstring("dvdf")
        assert self.value == 3
