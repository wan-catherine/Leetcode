from .Utility import ListNode

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        cur = head
        flag = False
        res = 0
        while cur:
            if cur.val not in g:
                flag = False
                cur = cur.next
                continue
            if flag == False:
                res += 1
                flag = True
            cur = cur.next
        return res