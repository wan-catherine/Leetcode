class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        nodes = [root]
        i = 0
        while True:
            node = nodes[i]
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            i += 1
            if i >= len(nodes):
                break
        length = len(nodes)
        for i in range(length, 1, -1):
            parent = nodes[i // 2 - 1]
            if i % 2 and parent.right != nodes[i-1]:
                return False
            if not i % 2 and parent.left != nodes[i-1]:
                return False
        return True


