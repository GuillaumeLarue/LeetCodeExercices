from dailyTemperatures.main import Solution


class TestDailyTemperatures:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
        assert self.value == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_two(self):
        so = Solution()
        self.value = so.dailyTemperatures([30, 40, 50, 60])
        assert self.value == [1, 1, 1, 0]

    def test_three(self):
        so = Solution()
        self.value = so.dailyTemperatures([30, 60, 90])
        assert self.value == [1, 1, 0]
