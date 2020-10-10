
class Solution(object):
    def delNodes_myself(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        def dfs(prev, node, val):
            if not node:
                return False
            if node.val != val:
                return dfs(node, node.left, val) or dfs(node, node.right, val)
            else:
                if prev:
                    if node == prev.left:
                        prev.left = None
                    else:
                        prev.right = None
                else:
                    stack.remove(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                return True

        stack = [root]
        for v in to_delete:
            i = 0
            while stack:
                if dfs(None, stack[i], v):
                    break
                i += 1
        return stack

    def delNodes(self, root, to_delete):
        deletes = set(to_delete)
        res = []

        def dfs(node, is_root):
            if not node:
                return None
            root_deleted = node.val in deletes
            if is_root and not root_deleted:
                res.append(node)
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            return None if root_deleted else node

        dfs(root, True)
        return res
