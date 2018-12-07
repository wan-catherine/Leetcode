# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        first = ListNode(val-1)
        first.next = head
        before = first
        temp = head
        while temp != None:
            if temp.val == val:
                before.next = temp.next
            else:
                before = temp
            temp = temp.next

        return first.next




