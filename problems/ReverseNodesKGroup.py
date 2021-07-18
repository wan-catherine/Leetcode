# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup_(self, head, k):
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

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        s, e = head, head
        first = True
        ans = None
        prev = dummy
        while e:
            t = k - 1
            while e and t:
                e = e.next
                t -= 1
            if t > 0 or not e:
                break
            while s != e:
                n = s.next
                s.next = e.next
                e.next = s
                s = n
            prev.next = s
            if first:
                ans = s
            first = False
            t = k
            while t:
                e = e.next
                s = s.next
                prev = prev.next
                t -= 1
        return ans

