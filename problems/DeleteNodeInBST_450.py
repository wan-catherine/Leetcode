# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        #root.val == key, there are several situations:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        #both of root left and right are not none, find the successor of the root
        right_node = root.right
        successor_node = right_node
        successor_parent_node = root

        while successor_node.left:
            successor_parent_node = successor_node
            successor_node = successor_node.left

        #find the successor node and his parent node , now more the successor node to replace the deleted node
        if successor_parent_node != root:
            successor_parent_node.left = successor_node.right
            successor_node.right = root.right
        successor_node.left = root.left
        return successor_node

    def deleteNode_not_passed(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        parent_node, deleted_node = self.query_key_parent_node(root,key)
        if not deleted_node:
            return root
        replace_node = self.find_replace_node(deleted_node)

        if parent_node:
            is_left = True if deleted_node == parent_node.left else False
            if is_left:
                parent_node.left = replace_node
            else:
                parent_node.right = replace_node

        if deleted_node == root:
            root = replace_node
        return root

    def find_replace_node(self, deleted_node):
        if not deleted_node.left and not deleted_node.right:
            return None
        if deleted_node.left and deleted_node.right:
            succssor = self.find_succssor(deleted_node)
            p_s, succssor = self.query_key_parent_node(deleted_node, succssor.val)
            if succssor != deleted_node.right:
                # deleted_node.right.left = succssor.right
                succssor.right = deleted_node.right
                # deleted_node.right = succssor
            succssor.left = deleted_node.left

            return succssor
        elif deleted_node.left:
            return deleted_node.left
        else:
            return deleted_node.right


    def find_succssor(self, deleted_node):
        current = deleted_node.right
        while current and current.left:
            current = current.left
        return current

    def query_key_parent_node(self, root, key):
        if root.val == key:
            return None, root
        parent_node = root
        if root.val < key:
            current = root.right
        else:
            current = root.left
        while current:
            if current.val == key:
                return parent_node, current
            parent_node = current
            if current.val < key:
                current = current.right
            else:
                current = current.left
        return parent_node, current
