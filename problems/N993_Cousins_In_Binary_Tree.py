from .Utility_Tree import TreeNode

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_res = self.get_parent_hight_for_node(None, root, 1, x)
        y_res = self.get_parent_hight_for_node(None, root, 1, y)

        if not x_res[0] or not y_res[0]:
            return False

        if x_res[1] == y_res[1] and x_res[2] != y_res[2]:
            return True

        return False

    def get_parent_hight_for_node(self, parent, current, h, x):
        if not current:
            return (False, h, parent)
        if current.val == x:
            return (True, h, parent)

        res = self.get_parent_hight_for_node(current, current.left, h+1, x)
        if not res[0]:
            res = self.get_parent_hight_for_node(current, current.right, h+1,x)
        return res