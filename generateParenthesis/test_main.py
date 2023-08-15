from generateParenthesis.main import Solution


class TestGenerateParenthesis:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.generateParenthesis(3)
        assert self.value == ["((()))", "(()())", "(())()", "()(())", "()()()"]

    def test_two(self):
        so = Solution()
        self.value = so.generateParenthesis(1)
        assert self.value == ["()"]

    def test_three(self):
        so = Solution()
        self.value = so.generateParenthesis(2)
        assert self.value == ["(())", "()()"]
