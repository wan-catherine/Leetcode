from collections import deque

from Utility_Tree import TreeNode, list_to_tree_node, null, treenode_to_list
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorder = self.get_preorder(root)
        inorder = self.get_inorder(root)
        return ','.join([str(i) for i in preorder+inorder])

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
                node.left = None
            else:
                res.append(node.val)
                stack.pop()
                if node.right:
                    stack.append(node.right)
                    node.right = None
        return res

    def get_preorder(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = [int(i) for i in data.split(',')]
        length = len(data) // 2
        preorder, inorder = data[:length], data[length:]
        return self.create_tree(preorder, inorder)

    def create_tree(self, preorder, inorder):
        if not preorder:
            return
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.create_tree(preorder[1:index+1], inorder[:index])
        root.right = self.create_tree(preorder[index+1:], inorder[index+1:])
        return root

ser = Codec()
deser = Codec()
root = list_to_tree_node([41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23])
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
print(treenode_to_list(ans))
