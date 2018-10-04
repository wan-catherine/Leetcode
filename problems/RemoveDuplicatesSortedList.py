# Definition for singly-linked list.
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

        i = head
        j = head.next
        while j != None:
            if j.val != i.val:
                i = j
            else:
                i.next = j.next
            j = j.next
        return head

