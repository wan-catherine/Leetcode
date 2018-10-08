# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        first = head
        small = ListNode(0)
        large = ListNode(0)
        i = small
        j = large
        while first != None:
            if first.val < x:
                i.next = first
                first = first.next
                i = i.next
                i.next = None
            else:
                j.next = first
                first = first.next
                j = j.next
                j.next = None
        i.next = large.next
        return small.next
