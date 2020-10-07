"""
Use BFS
First need to find all node's parent to convert a directed graph(tree) to undirected graph.
"""
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parents = {}

        def get_parents(root):
            if root.left:
                parents[root.left] = root
                get_parents(root.left)
            if root.right:
                parents[root.right] = root
                get_parents(root.right)

        if not K:
            return [target.val]
        get_parents(root)
        # print(len(parents))
        stack = [target]
        visited = set()
        while K:
            new_stack = []
            for node in stack:
                if node.left and node.left not in visited:
                    new_stack.append(node.left)
                if node.right and node.right not in visited:
                    new_stack.append(node.right)
                if node != root and parents[node] not in visited:
                    new_stack.append(parents[node])
                visited.add(node)
            K -= 1
            stack = new_stack
        return [node.val for node in stack]


