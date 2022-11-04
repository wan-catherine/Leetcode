import bisect
import collections
from typing import Optional, List

from problems.Utility_Tree import TreeNode

"""
Key point:
    There are two situations : 
    1. when the deleted node has siblings , then the answer will be the max(siblings)
    2. if it doesn't have siblings , then its parents.
    
"""


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int], siblings=None) -> List[int]:
        upc, downc = collections.defaultdict(int), collections.defaultdict(int)
        levels = collections.defaultdict(set)
        pt = collections.defaultdict(int)
        def dfs(node, up, parent):
            if not node:
                return -1
            if node != root:
                pt[node.val] = parent.val
            upc[node.val] = up
            levels[up].add(node.val)
            l, r = dfs(node.left, up+1, node), dfs(node.right, up+1, node)
            downc[node.val] = max(l, r) + 1
            return downc[node.val]

        dfs(root, 0, None)

        status = collections.defaultdict(list)
        for lel, nodes in levels.items():
            for node in nodes:
                bisect.insort_left(status[lel], (-(upc[node] + downc[node]), node))


        res = []
        for qe in queries:
            ans = upc[pt[qe]]
            if qe != status[upc[qe]][0][1]:
                ans = max(ans, -status[upc[qe]][0][0])
            elif len(status[upc[qe]]) > 1:
                ans = max(ans, -status[upc[qe]][1][0])
            res.append(ans)
        return res

