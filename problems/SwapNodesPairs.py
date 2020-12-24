# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs_(self, head):
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

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first = head
        previous = ListNode(0)
        previous.next = head
        flag = False
        while first:
            second = first.next
            if not second:
                break
            first.next = second.next
            second.next = first
            previous.next = second
            if not flag:
                head = second
                flag = True
            previous = first
            first = first.next
        return head
