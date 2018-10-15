class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or head.next == None:
            return head

        p = head
        if m == 1:
            q = p
            count = 1
        else:
            count = 2
            q = p.next
            while count < m:
                p = p.next
                q = q.next
                count += 1

        k = q.next
        t = k.next if k != None else None

        while count < n:
            k.next = q
            q = k
            k = t
            t = t.next if t != None else None
            count += 1
        if m > 1:
            p.next.next = k
            p.next = q
        else:
            p.next = k
            head = q

        return head