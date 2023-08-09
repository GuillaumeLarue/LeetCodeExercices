from isPalindrome.main import Solution


class TestIsPalindrome:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.isPalindrome("A man, a plan, a canal: Panama")
        assert self.value

    def test_two(self):
        so = Solution()
        self.value = so.isPalindrome("race a car")
        assert not self.value

    def test_three(self):
        so = Solution()
        self.value = so.isPalindrome(" ")
        assert self.value
