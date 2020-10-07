class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parents = {}
        heights = {}
        def get_parents(node):
            if not node:
                return
            if node.left:
                parents[node.left] = node
                get_parents(node.left)
            if node.right:
                parents[node.right] = node
                get_parents(node.right)

        def get_heights(node, h):
            if not node:
                return
            heights[node] = h
            if node.left:
                get_heights(node.left, h+1)
            if node.right:
                get_heights(node.right, h+1)

        get_parents(root)
        get_heights(root, 1)

        maximum = max(heights.values())
        nodes = []
        for node, height in heights.items():
            if height == maximum:
                nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        while True:
            new_parents = set(parents[node] for node in nodes)
            if len(new_parents) > 1:
                nodes = new_parents
            else:
                return list(new_parents)[0]