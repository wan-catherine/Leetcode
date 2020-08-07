import collections

from problems.Utility_Tree import TreeNode

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.x_y_mapping = collections.defaultdict(list)
        self.helper(root, 0 , 0)
        res = []

        keys = sorted(self.x_y_mapping.keys())
        for x in keys:
            # here is the key part , sort by multiple keys
            # use -x[1] same as reverse, but it much faster
            self.x_y_mapping[x].sort(key=lambda x: (-x[1], x[0]))
            x_level = [val for val, y in self.x_y_mapping[x]]
            res.append(x_level)
        return res

    def helper(self, node, x, y):
        self.x_y_mapping[x].append((node.val, y))
        if node.left:
            self.helper(node.left, x-1, y-1)
        if node.right:
            self.helper(node.right, x+1, y-1)
