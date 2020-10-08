"""
Key point :
    only odd N can have validate solution.
    recursive for the result of the function.
"""
from .Utility_Tree import TreeNode
class Solution(object):
    def __init__(self):
        self.memo = {}

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res = []
        if not N%2:
            return res
        if N == 1:
            return [TreeNode(0)]
        if N in self.memo:
            return self.memo[N]

        for i in range(1,N,2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)

        self.memo[N] = res
        return res

