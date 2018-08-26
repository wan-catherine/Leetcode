# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = []
        i = 0
        while head != None:
            l.append(head.val)
            i += 1
            if i % k == 0:
                l[i - k:i] = l[i - k:i][::-1]
            head = head.next
        head = ListNode(0)
        temp = head
        for i in l:
            temp.next = ListNode(i)
            temp = temp.next

        return head.next

