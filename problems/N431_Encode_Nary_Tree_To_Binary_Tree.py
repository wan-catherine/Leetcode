"""
For any node in the N_ary tree:
    his first child to Binary Tree's left child
    all other children will be this first child(left child of BT)'s right child.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return
        t = TreeNode(root.val)
        if root.children:
            t.left = self.encode(root.children[0])
        cur = t.left
        for node in root.children[1:]:
            cur.right = self.encode(node)
            cur = cur.right
        return t

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return
        root = Node(data.val, [])
        cur = data.left
        while cur:
            root.children.append(self.decode(cur))
            cur = cur.right
        return root