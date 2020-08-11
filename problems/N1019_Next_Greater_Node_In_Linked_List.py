from collections import deque

from .Utility import ListNode

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        res = [0]*length
        cur = head
        index = 0
        stack = deque()
        while cur:
            while stack and stack[-1][0] < cur.val:
                value, i = stack.pop()
                res[i] = cur.val
            stack.append((cur.val, index))
            index += 1
            cur = cur.next
        return res
