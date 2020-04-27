# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes_timeout(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = [root]
        next = []
        res = 0
        while len(stack) > 0:
            temp = []
            for node in stack:
                temp.append(node.val)
                if node.left != None:
                    next.append(node.left)
                if node.right != None:
                    next.append(node.right)
            res+=len(temp)
            stack = next
            next = []

        return res

    def countNodes_dfs(self, root):
        def dfs_l(r):
            if r.left == None:
                return 1
            else:
                return dfs_l(r.left) + 1

        def dfs_r(r):
            if r.right == None:
                return 1
            else:
                return dfs_r(r.right) + 1

        def comp_l_r(r):
            if r == None:
                return 0
            else:
                l_h = dfs_l(r)
                r_h = dfs_r(r)
                if l_h == r_h:
                    return 2 ** l_h - 1
                else:
                    return comp_l_r(r.left) + comp_l_r(r.right) + 1

        return comp_l_r(root)

    def countNodes(self, root):
        n_nodes = 0
        height = self.get_height(root)
        while root:
            if self.get_height(root.right) == height - 1:
                n_nodes += 2 ** (height - 1)
                root = root.right
            else:
                n_nodes += 2 ** (height - 2)
                root = root.left
            height -= 1
        return n_nodes

    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height


# it's a complete tree , so we can check the height of left and right subtree.
# if height(left subtree) == height(right subtree), it means the left subtree is a full binary tree
# if height(left subtree) != height(right subtree), it means the right subtree is a full binary tree
# so we can recursively to check the subtree

    def count_nodes(self, root):
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:
            return self.count_nodes(root.right) + 1 << left_height
        else:
            return self.count_nodes(root.left) + 1 << right_height
