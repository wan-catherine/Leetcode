from .Utility_Tree import TreeNode

class Solution:
    def kthSmallest_slow(self, root: TreeNode, k: int) -> int:
        self.vals = []
        self.in_order(root)
        return self.vals[k-1]

    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        self.vals.append(root.val)
        if root.right:
            self.in_order(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        values = []
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                values.append(cur.val)
                if len(values) == k:
                    return values[-1]
                cur = cur.right
            else:
                break
