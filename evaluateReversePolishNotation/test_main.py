from evaluateReversePolishNotation.main import Solution


class TestEvaluateReversePolishNotation:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.evalRPN(["2", "1", "+", "3", "*"])
        assert self.value == 9

    def test_two(self):
        so = Solution()
        self.value = so.evalRPN(["4", "13", "5", "/", "+"])
        assert self.value == 6

    def test_three(self):
        so = Solution()
        self.value = so.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        assert self.value == 22

    def test_four(self):
        so = Solution()
        self.value = so.evalRPN(["0", "3", "/"])
        assert self.value == 0

    def test_five(self):
        so = Solution()
        self.value = so.evalRPN(["-4", "2", "-"])
        assert self.value == -6
