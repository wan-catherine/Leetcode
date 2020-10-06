from collections import deque

from .Utility_Tree import TreeNode
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        inorder = self.get_inorder(root)
        preorder = self.get_preorder(root)
        return ''.join(preorder+inorder)

    def get_inorder(self, root):
        if not root:
            return []
        res = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack[-1]
            if node.left:
                stack.append(node.left)
            else:
                res.append(node.val)
                stack.popleft()
                if node.right:
                    stack.append(node.right)
        return res

    def get_


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """