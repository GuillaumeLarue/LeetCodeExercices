from reverseList.main import Solution, list2ListNode, listNode2List


class TestUtilsFunctions:
    def test_one(self):
        ln = list2ListNode([1, 2, 3, 4, 5])
        l = listNode2List(ln)
        assert l == [1, 2, 3, 4, 5]

    def test_two(self):
        ln = list2ListNode([1, 2])
        l = listNode2List(ln)
        assert l == [1, 2]

    def test_three(self):
        ln = list2ListNode([])
        l = listNode2List(ln)
        assert l == []


class TestReverseList:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.reverseList(list2ListNode([1, 2, 3, 4, 5]))
        assert listNode2List(self.value) == [5, 4, 3, 2, 1]

    def test_two(self):
        so = Solution()
        self.value = so.reverseList(list2ListNode([1, 2]))
        assert listNode2List(self.value) == [2, 1]

    def test_three(self):
        so = Solution()
        self.value = so.reverseList(list2ListNode([]))
        assert listNode2List(self.value) == []
