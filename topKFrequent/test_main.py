from topKFrequent.main import Solution


class TestTopKFrequent:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
        assert self.value == [1,2]

    def test_two(self):
        so = Solution()
        self.value = so.topKFrequent(nums = [1], k = 1)
        assert self.value == [1]
