from .Utility import ListNode

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        cur = root
        while cur:
            length += 1
            cur = cur.next

        divisor, remainder = divmod(length, k)
        res = []
        cur, head = root, root
        new_d, new_r = 1, 0
        while cur:
            if divisor == 0:
                next = cur.next
                res.append(cur)
                cur.next = None
                cur = next
                continue
            if new_d == divisor:
                new_d = 1
                if new_r < remainder:
                    new_r += 1
                    next = cur.next.next
                    cur.next.next = None
                    res.append(head)
                    head = next
                    cur = next
                else:
                    res.append(head)
                    head = cur.next
                    cur.next = None
                    cur = head
            else:
                cur = cur.next
                new_d += 1
        left = k - len(res)
        while left:
            res.append(None)
            left -= 1
        return res


