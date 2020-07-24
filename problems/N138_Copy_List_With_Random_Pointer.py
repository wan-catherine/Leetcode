# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        copied = {}
        cur = head
        while cur:
            copied[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                copied[cur].next = copied[cur.next]
            if cur.random:
                copied[cur].random = copied[cur.random]
            cur = cur.next

        return copied[head]