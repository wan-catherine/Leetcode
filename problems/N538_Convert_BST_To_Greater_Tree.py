class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = [root]
        prev = 0
        visited = set()
        visited.add(root)
        visited.add(None)
        while stack:
            node = stack[-1]
            if node.left in visited and node.right in visited:
                node.val += prev
                prev = node.val
                stack.pop()
            if node.right and node.right not in visited:
                stack.append(node.right)
                visited.add(node.right)
                continue
            if node.left and node.left not in visited:
                node.val += prev
                prev = node.val
                stack.pop()
                stack.append(node.left)
                visited.add(node.left)
                continue
        return root
