# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        before = head
        chain = head
        after = head.next
        if after != None:
            head = after

        while after != None:
            chain.next = after
            before.next = after.next
            after.next = before
            chain = before
            before = before.next
            if before == None:
                break
            after = before.next

        return head