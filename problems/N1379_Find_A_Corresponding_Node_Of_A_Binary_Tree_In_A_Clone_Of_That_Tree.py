class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        steps = 1

        stack = [original]
        while stack:
            node = stack.pop()
            if node == target:
                break
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            steps += 1

        stack = [cloned]
        while stack:
            node = stack.pop()
            if steps == 0:
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            steps -= 1
