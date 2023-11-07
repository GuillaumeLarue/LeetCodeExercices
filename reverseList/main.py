from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


def listNode2List(ln: ListNode) -> List:
    res = []
    while ln is not None:
        res.append(ln.value)
        ln = ln.next
    return res


def list2ListNode(l: List) -> Optional[ListNode]:
    if len(l) == 0:
        return None
    head = ListNode(l[0])
    res = head
    for i in range(1, len(l)):
        tmp = ListNode(l[i])
        head.next = tmp
        head = head.next
    return res


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            node_tmp = head
            head = head.next
            node_tmp.next = prev
            prev = node_tmp
        return prev
