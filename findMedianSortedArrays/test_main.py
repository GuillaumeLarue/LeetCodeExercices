from findMedianSortedArrays.main import Solution


class TestFindMedianSortedArrays:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.findMedianSortedArrays([1, 3], [2])
        assert self.value == 2.00000

    def test_two(self):
        so = Solution()
        self.value = so.findMedianSortedArrays([1,2], [3,4])
        assert self.value == 2.50000

    def test_three(self):
        so = Solution()
        self.value = so.findMedianSortedArrays([2, 3,4,54, 6464], [1, 3,4,5, 6, 22222])
        assert self.value == 4.00000

