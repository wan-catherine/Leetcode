"""
We only know preorder here , so each time after comparing root,
we only compare the left node, if it's same, then compare right node.
If not , then flip and then compare which means compare it's right node first , then left node.

The key point here is the self.index!!!
"""
class Solution(object):
    def __init__(self):
        self.index = 0

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        def check(node, arr, li):
            if not node :
                return True
            if node.val != arr[self.index]:
                return False
            self.index += 1
            if node.left and node.left.val != arr[self.index]:
                li.append(node.val)
                return check(node.right, arr, li) and check(node.left, arr, li)
            return check(node.left, arr, li) and check(node.right, arr, li)

        res = []
        if check(root, voyage, res):
            return res
        else:
            return [-1]
