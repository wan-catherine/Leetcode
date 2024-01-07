# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        fake = ListNode(head.val - 1)
        fake.next = head
        cur = head
        before = fake
        while cur.next != None:
            if cur.val == cur.next.val:
                cur = cur.next
            else:
                if before.next != cur:
                    before.next = cur.next
                else:
                    before = before.next
                cur = cur.next
                if cur.next != None and cur.val != cur.next.val:
                    before = cur

        else:
            if before.next != cur:
                before.next = None
        return fake.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode()
        d = res
        val = None
        cur = head
        t = 0
        while cur:
            t = cur
            while t and t.next and t.next.val == cur.val:
                t = t.next
            if t == cur:
                d.next = cur
                d = d.next
            cur = t.next
        d.next = cur
        return res.next


        