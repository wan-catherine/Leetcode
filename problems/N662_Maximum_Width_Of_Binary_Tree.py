import collections

from .Utility_Tree import TreeNode

class Solution(object):
    def widthOfBinaryTree_timeout(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        res = 1
        stack = [root]
        while True:
            level = []
            flag = False
            for node in stack:
                if not node:
                    level.append(None)
                    level.append(None)
                else:
                    level.append(node.left)
                    level.append(node.right)
                    if node.left or node.right:
                        flag = True
            length = len(level)
            for i in range(length-1, -1, -1):
                if level[i]:
                    res = max(res, i + 1)
                    break

            while level:
                if not level[-1]:
                    level.pop()
                else:
                    break
            stack = level
            if not flag:
                return res

    def widthOfBinaryTree_(self, root):
        if not root:
            return 0

        stack = collections.deque([(root, 0, 1)])
        old_level, old_num = 0, 1
        res = 1
        while stack:
            node, level, pos = stack.popleft()
            if level > old_level:
                old_level, old_num = level, pos
            res = max(res, pos - old_num + 1)
            if node.left:
                stack.append((node.left, level+1, 2*pos))
            if node.right:
                stack.append((node.right, level+1, 2*pos+1))
        return res

    """
    Think about heap which is a complete binary tree. for any index i, its left child is at : 2*i, and its right child is at : 2*i + 1. 
    So this way we can give each node a position. 
    But this position might be super big 2**3000 at most. 
    So we can use diff . each position - the leftest position. 
    """
    def widthOfBinaryTree(self, root):
        stack = [(root, 0)]
        res = 1
        while stack:
            new_stack = []

            for node, idx in stack:
                if node.left:
                    new_stack.append((node.left, idx*2))
                if node.right:
                    new_stack.append((node.right, idx*2 + 1))
            if not new_stack:
                break
            diff = new_stack[0][1]
            stack = [(node, idx - diff) for node, idx in new_stack]
            res = max(res, stack[-1][1] + 1)
        return res


