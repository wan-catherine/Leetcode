"""
serialize each node and compare the serialization str.
We use serialization gives each node a id.
Here we try to give each node a key (node.val, left_id, right_id).
"""
import collections
from typing import List, Optional

from Utility_Tree import TreeNode


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
        print(mapping)
        return res

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mapping = collections.defaultdict(TreeNode)
        res = []
        visited = set()

        def dfs(node):
            nonlocal res
            if not node:
                return ['#']
            ans = [str(node.val)]
            ans.extend(dfs(node.left))
            ans.extend(dfs(node.right))
            key = ','.join(ans)
            if key in mapping:
                if key not in visited:
                    visited.add(key)
                    res.append(node)
            else:
                mapping[key] = node
            return ans

        dfs(root)
        return res
