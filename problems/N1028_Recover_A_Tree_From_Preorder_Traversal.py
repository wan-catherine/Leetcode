from .Utility_Tree import TreeNode
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        i, length = 0, len(S)
        def helper(cur):
            nonlocal i, S, length
            num = 0
            while i < length and S[i] != '-':
                num = num*10 + int(S[i])
                i += 1
            root = TreeNode(num)
            if i == length:
                return root
            count = 0
            while i < length and S[i] == '-':
                count += 1
                i += 1
            if count == cur + 1:
                root.left = helper(count)
            else:
                i -= count
                return root

            count = 0
            while i < length and S[i] == '-':
                count += 1
                i += 1
            if count == cur + 1:
                root.right = helper(count)
            else:
                i -= count
            return root
        return helper(0)