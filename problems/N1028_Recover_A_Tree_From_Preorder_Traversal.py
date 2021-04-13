import collections

from .Utility_Tree import TreeNode
class Solution(object):
    def recoverFromPreorder_before(self, S):
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

    def recoverFromPreorder(self, S: str) -> TreeNode:
        mapping = collections.defaultdict(list)
        i, length = 0, len(S)
        count = 0
        while i < length:
            if S[i] != '-':
                j = i
                while j+1 < length and S[j+1] != '-':
                    j += 1
                val = int(S[i:j+1])
                mapping[count].append((i,val))
                count = 0
                i = j + 1
            else:
                count = 1
                while i+1 < length and S[i+1] == '-':
                    i += 1
                    count += 1
                i += 1
        idx, v = mapping[0].popleft()
        root = TreeNode(v)
        key = 1
        stack = [(idx,root)]
        while key < len(mapping):
            dq = mapping[key]
            new_stack = []
            for idx, node in stack:
                while dq and dq[-1][0] > idx:
                    i, v = dq.pop()
                    if dq and dq[-1][0] > idx:
                        if not node.right:
                            node.right = TreeNode(v)
                            new_stack.append((i, node.right))
                    else:
                        if not node.left:
                            node.left = TreeNode(v)
                            new_stack.append((i, node.left))
            stack = new_stack
            key += 1
        return root