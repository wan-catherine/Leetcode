# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        head = ListNode(0)
        temp = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else :
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next

        if l1 != None:
            temp.next = l1
        elif l2 != None:
            temp.next = l2

        return head.next