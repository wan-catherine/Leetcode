from problems.Utility_Tree import TreeNode,list_to_tree_node, null, treenode_to_list

"""
This problem seems similar like : 449. Serialize and Deserialize BST, but actually it can't use the same preorder/inorder to deserialize. 
Because this time it's only a binary tree which means the vals are not unique. 

Another point here is try to use iter(), next() to avoid the global index variable. so Pythonic!!!
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def get_preorder(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            get_preorder(root.left)
            get_preorder(root.right)
        get_preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(','))
        def helper():
            val = next(vals)
            if val == '#':
                return
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            return root
        root = helper()
        return root

root = list_to_tree_node([1,2,3,null,null,4,5])
ser = Codec()
deser = Codec()
res = ser.serialize(root)
print(res)
ans = deser.deserialize(res)
print(treenode_to_list(ans))
