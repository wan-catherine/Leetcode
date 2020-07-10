# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return

        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy
        while stack:
            node = stack.pop()

            node.prev = prev
            prev.next = node

            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None

            prev = node

        dummy.next.prev = None

        return head