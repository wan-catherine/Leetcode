# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head

        count = 1
        tail = head
        while tail.next != None:
            count += 1
            tail = tail.next

        m = k % count
        if m == 0:
            return head

        i = 0
        point = head
        newTail = head
        while point.next != None:
            if i == count - m - 1:
                newTail = point
            if i < count - m:
                i += 1
                point = point.next
            else:
                break

        tail.next = head
        newTail.next = None
        head = point
        return head







