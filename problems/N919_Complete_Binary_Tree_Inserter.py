"""
The key point here is how to find the parent node.
It's a complete binary tree which means for ith node (1-index), it's left child is 2*i, and right child is 2*i + 1.
So we can use this feature to quickly find the parent node.
"""
from collections import deque

from problems.Utility_Tree import TreeNode, list_to_tree_node
class CBTInserter_myself(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.height = self.get_height(root)
        self.incompleted = None
        self.leaves = deque()
        self.get_incompleted(root, 1)

    def get_incompleted(self, node, h):
        if not node:
            return
        if not node.left and not node.right:
            self.leaves.append([node, h])
        elif not node.right:
            self.incompleted = [node, h]
        self.get_incompleted(node.left, h+1)
        self.get_incompleted(node.right, h+1)

    def get_height(self, node):
        root = node
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        if self.incompleted:
            self.incompleted[0].right = TreeNode(v)
            self.leaves.append([self.incompleted[0].right, self.incompleted[1] + 1])
            val = self.incompleted[0].val
            self.incompleted = None
            return val
        the_node = None
        for li in self.leaves:
            if li[1] == self.height - 1:
                the_node = li
                break
        if the_node:
            the_node[0].left = TreeNode(v)
            self.incompleted = the_node
            self.leaves.remove(the_node)
            self.leaves.append([the_node[0].left, the_node[1]+1])
            return the_node[0].val

        node, h = self.leaves[0]
        node.left = TreeNode(v)
        self.height += 1
        self.incompleted = [node, h]
        self.leaves.popleft()
        self.leaves.append([self.incompleted[0].left, h+1])
        return node.val


    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [root]
        i = 0
        while True:
            node = self.nodes[i]
            if node.left:
                self.nodes.append(node.left)
            if node.right:
                self.nodes.append(node.right)
            i += 1
            if i >= len(self.nodes):
                break

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        self.nodes.append(node)
        parent = self.nodes[len(self.nodes) // 2 - 1]
        if len(self.nodes) % 2:
            parent.right = node
        else:
            parent.left = node
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]

root = list_to_tree_node([1,2,3,4,5])
obj = CBTInserter(root)
print(obj.insert(6))
print(obj.insert(7))
print(obj.insert(8))
print(obj.insert(9))
print(obj.insert(10))
print(obj.insert(11))
print(obj.insert(12))
param_2 = obj.get_root()