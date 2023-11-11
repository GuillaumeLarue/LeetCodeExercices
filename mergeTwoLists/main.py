from typing import Optional

from reverseList.main import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return None

    def mergeTwoLists_1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # To complex, not in place
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1
        res = None
        head = None
        first = True
        while list1 is not None and list2 is not None:
            new_node = ListNode(0)
            if list1.value == list2.value:
                new_node.value = list1.value
                list1 = list1.next
            elif list1.value > list2.value:
                new_node.value = list2.value
                list2 = list2.next
            else:  # list1.value < list2.value:
                new_node.value = list1.value
                list1 = list1.next
            if res == None and first:
                res = new_node
                head = res
                # res = res.next
                first = False
            else:
                res.next = new_node
                res = res.next
        if list1 is None and list2 is not None:
            res.next = list2
        if list2 is None and list1 is not None:
            res.next = list1
        return head
