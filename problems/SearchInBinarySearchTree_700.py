# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        current = root
        while current:
            if current.val == val:
                return current
            if val > current.val:
                current = current.right
            else:
                current = current.left
        return current