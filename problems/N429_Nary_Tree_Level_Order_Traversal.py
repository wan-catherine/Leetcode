class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type
        root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            new_stack = []
            temp = []
            for node in stack:
                temp.append(node.val)
                if not node.children:
                    continue
                for child in node.children:
                    if not child:
                        continue
                    new_stack.append(child)
            stack = new_stack
            res.append(temp)
        return res
