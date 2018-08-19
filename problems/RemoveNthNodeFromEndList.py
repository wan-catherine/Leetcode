# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        beforeNode = head
        index = 1
        endNode = head
        deleteNode = head
        while endNode.next != None:
            endNode = endNode.next

            if index > n:
                beforeNode = beforeNode.next

            if index >= n:
                deleteNode = deleteNode.next

            index += 1

        if beforeNode == deleteNode:
            head = head.next
        else:
            beforeNode.next = deleteNode.next
        return head