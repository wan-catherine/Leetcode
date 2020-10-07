from problems.Utility_Tree import TreeNode

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def get_height(root, h):
            if not root:
                return h
            left_h = get_height(root.left, h)
            right_h = get_height(root.right, h)
            return max(left_h, right_h) + 1
        height = get_height(root, 0)
        rows, cols = height, 2**height - 1
        res = [[""]*cols for _ in range(rows)]

        def print_(root, i, j, row):
            if not root:
                return
            col = i + (j-i)//2
            res[row][col] = str(root.val)
            print_(root.left, i, col-1, row+1)
            print_(root.right, col+1, j, row+1)
        print_(root, 0, cols-1, 0)
        # print(res)
        return res

