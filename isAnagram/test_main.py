from isAnagram.main import Solution


class TestIsAnagram:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.isAnagram("aea", "aae")
        assert self.value == True

    def test_two(self):
        so = Solution()
        self.value = so.isAnagram("dddd", "eaz")
        assert self.value == False

    def test_three(self):
        so = Solution()
        self.value = so.isAnagram("eeeee", "eeeee")
        assert self.value == True
