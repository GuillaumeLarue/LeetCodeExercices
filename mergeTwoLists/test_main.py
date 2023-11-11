from mergeTwoLists.main import Solution
from reverseList.main import list2ListNode, listNode2List


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


class TestMergeTwoLists:
    value = 0

    def test_one(self):
        so = Solution()
        self.value = so.mergeTwoLists(list2ListNode([1, 2, 4]), list2ListNode([1, 3, 4]))
        assert listNode2List(self.value) == [1, 1, 2, 3, 4, 4]

    def test_two(self):
        so = Solution()
        self.value = so.mergeTwoLists(list2ListNode([0]), list2ListNode([]))
        assert listNode2List(self.value) == [0]

    def test_three(self):
        so = Solution()
        self.value = so.mergeTwoLists(list2ListNode([1, 2, 4, 6, 7]), list2ListNode([1, 3, 4]))
        assert listNode2List(self.value) == [1, 1, 2, 3, 4, 4, 6, 7]
