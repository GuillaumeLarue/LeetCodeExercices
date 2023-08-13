from validesParentheses.main import Solution


class TestValidesParentheses:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.isValid(s="()")
        assert self.value

    def test_two(self):
        so = Solution()
        self.value = so.isValid(s="()[]{}")
        assert self.value

    def test_three(self):
        so = Solution()
        self.value = so.isValid(s = "(]")
        assert not self.value