from .Utility_Tree import TreeNode
"""
It asks use constant space. So we can't use hashmap to do so. 

According to the statement of this problem, the same val should be near each other when we traverse as in-order . 
So we set count and maximum and update the res.
"""
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count, maximum = 0, 0
        res = []
        previous = None

        def helper(node):
            nonlocal count, maximum, res, previous
            if not node:
                return
            helper(node.left)
            if not previous:
                count, maximum = 1, 1
            elif previous.val == node.val:
                count += 1
            else:
                count = 1
            if count == maximum:
                res.append(node.val)
            elif count > maximum:
                maximum = count
                res = [node.val]
            previous = node
            helper(node.right)
        helper(root)
        return res