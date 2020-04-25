# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return self.helper(root)
        return self.max_depth_stack(root)

    def helper(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 1

        nleft = self.helper(node.left)
        nright = self.helper(node.right)

        nsubTree = nleft if nleft > nright else nright
        return nsubTree + 1

    #DFS by using two stacks : one stack is for the nodes, another is for the depth , those two are matched.
    def max_depth_stack(self, root):
        if not root:
            return 0
        max_depth = 0
        depth_stack = [1]
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            depth = depth_stack.pop()
            print(f"node:{node.val} depth:{depth}")
            max_depth = max_depth if max_depth > depth else depth
            if not node:
                continue
            if node.right:
                node_stack.append(node.right)
                depth_stack.append(depth + 1)
            if node.left:
                node_stack.append(node.left)
                depth_stack.append(depth + 1)
        return  max_depth







