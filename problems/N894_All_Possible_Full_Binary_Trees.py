"""
Key point :
    only odd N can have validate solution.
    recursive for the result of the function.
"""
from .Utility_Tree import TreeNode
class Solution(object):
    def __init__(self):
        self.memo = {}

    def allPossibleFBT_best(self, N):
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

    # update at 20210106
    def allPossibleFBT_complexity(self, N: int) :
        if not N % 2:
            return []

        arr = set([TreeNode(0)])

        def copy_tree(root):
            if root:
                r = TreeNode(0)
                r.left = copy_tree(root.left)
                r.right = copy_tree(root.right)
                return r
            else:
                return

        def encode_tree(root):
            res = []
            stack = [root]
            while stack:
                node = stack.pop()
                if isinstance(node, TreeNode):
                    res.append(str(node.val))
                    if node.right:
                        stack.append(node.right)
                    else:
                        stack.append('#')
                    if node.left:
                        stack.append(node.left)
                    else:
                        stack.append('#')
                else:
                    res.append(node)
            return ''.join(res)

        def create_tree(root, node, array, seq):
            if not node.left and not node.right:
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                n = copy_tree(root)
                key = encode_tree(n)
                if key not in seq:
                    seq.add(key)
                    array.add(n)
                node.left, node.right = None, None
                return
            if node.left:
                create_tree(root, node.left, array, seq)
            if node.right:
                create_tree(root, node.right, array, seq)

        for k in range(3, N + 1, 2):
            ans = set()
            seq = set()
            for node in arr:
                create_tree(node, node, ans, seq)
            arr = ans
        return arr

    # dp
    def allPossibleFBT(self, N):
        if not N % 2:
            return []

        memo = {0: [], 1: [TreeNode(0)]}
        if N in memo:
            return memo[N]

        for n in range(3, N + 1, 2):
            res = []
            for i in range(1, n, 2):
                # print(i, n-i-1, n)
                left = memo[i]
                right = memo[n - i - 1]
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            memo[n] = res
        return memo[N]