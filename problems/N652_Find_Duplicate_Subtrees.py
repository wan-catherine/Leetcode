"""
serialize each node and compare the serialization str.
We use serialization gives each node a id.
Here we try to give each node a key (node.val, left_id, right_id).
"""
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        mapping = {}
        count = {}
        ids = {}
        def get_key(node):
            if not node:
                return 0
            key = (node.val, get_key(node.left), get_key(node.right))
            if key in mapping:
                count[key] += 1
                if count[key] == 2:
                    res.append(ids[key])
                return mapping[key]
            mapping[key] = len(mapping) + 1
            count[key] = 1
            ids[key] = node
            return mapping[key]
        get_key(root)
        return res



