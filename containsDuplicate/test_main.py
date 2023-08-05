from containsDuplicate.main import Solution


class TestContainsDuplicate:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.containsDuplicate([1, 3])
        assert self.value == False

    def test_two(self):
        so = Solution()
        self.value = so.containsDuplicate([1, 2])
        assert self.value == False

    def test_three(self):
        so = Solution()
        self.value = so.containsDuplicate([2, 2, 4, 54, 6464])
        assert self.value == True
