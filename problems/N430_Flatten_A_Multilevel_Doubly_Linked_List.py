# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten_before(self, head):
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

    def flatten(self, head):
        if not head:
            return head

        cur = head
        self.dfs(cur)
        return head

    """
    Spent a lot of time one this function. 
    Three key points:
        1. return the tail node 
        2. when node has child, first find the child level's trail node 
        3. after from child to the last level, still remember to call self.dfs
    """
    def dfs(self, node):
        if node.child:
            last_node = self.dfs(node.child)
            next_node = node.next
            child = node.child
            node.next = child
            child.prev = node
            node.child = None
            last_node.next = next_node
            if next_node:
                next_node.prev = last_node
                return self.dfs(next_node)
            else:
                return last_node
        elif node.next:
            return self.dfs(node.next)
        else:
            return node


