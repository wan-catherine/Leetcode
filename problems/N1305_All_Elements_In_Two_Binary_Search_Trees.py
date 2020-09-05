from .Utility_Tree import TreeNode

class Solution(object):
    def getAllElements_list(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr1, arr2 = [], []
        self.helper(root1, arr1)
        self.helper(root2, arr2)
        if not arr1:
            return arr2
        if not arr2:
            return arr1

        res = []
        p1, p2 = 0, 0
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                res.append(arr1[p1])
                p1 += 1
            else:
                res.append(arr2[p2])
                p2 += 1
        if p1 < len(arr1):
            res.extend(arr1[p1:])
        elif p2 < len(arr2):
            res.extend(arr2[p2:])
        return res

    def helper(self, root, res):
        if not root:
            return res
        if not root.left and not root.right:
            res.append(root.val)
            return
        if root.left:
            self.helper(root.left, res)
        res.append(root.val)
        if root.right:
            self.helper(root.right, res)

    def getAllElements(self, root1, root2):
        arr1, arr2 = [], []
        res = []
        while root1 or root2 or arr1 or arr2:
            while root1:
                arr1.append(root1)
                root1 = root1.left
            while root2:
                arr2.append(root2)
                root2 = root2.left

            if not arr2 or arr1 and arr1[-1].val <= arr2[-1].val:
                node = arr1.pop()
                res.append(node.val)
                root1 = node.right
            else:
                node = arr2.pop()
                res.append(node.val)
                root2 = node.right
        return res


