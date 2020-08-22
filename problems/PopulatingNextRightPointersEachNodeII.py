# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_before(self, root):
        before = None
        current = root

        while current != None:
            if before == None:
                before = current
                current = current.left if current.left != None else current.right
                continue
            node = current
            if current == before.left and before.right != None:
                node.next = before.right
                node = node.next
            while before.next != None:
                before = before.next
                if before.left != None:
                    node.next = before.left
                    node = node.next
                if before.right != None:
                    node.next = before.right
                    node = node.next
            while current != None and current.left == None and current.right == None:
                current = current.next

            before = current
            if current != None:
                current = current.left if current.left != None else current.right

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        parent = root
        while parent:
            new_parent = None
            if not parent.left and not parent.right:
                parent = parent.next
                continue
            if parent.left:
                new_parent = parent.left
                cur = parent.left
                if parent.right:
                    cur.next = parent.right
                    cur = cur.next
            else:
                cur = parent.right
                new_parent = parent.right

            node = parent.next
            while node:
                if not node.left and not node.right:
                    node = node.next
                    continue
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                node = node.next
            parent = new_parent
        return root