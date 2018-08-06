# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        k = 0
        rtype = l3 = ListNode(0)
        while l1 or l2 or k != 0:
            l3.next = ListNode(0)
            l3 = l3.next
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            l3.val = (p1 + p2 + k) % 10
            k = (p1 + p2 + k) // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return rtype.next