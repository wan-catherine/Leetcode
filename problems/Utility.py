class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree_from_list(nodes):
    stack = []
    for i in range(len(nodes)):
        if not nodes[i]:
            continue
        treenode = TreeNode(nodes[i])
        if not stack:
            stack.append(treenode)
        if i + 2 < len(nodes) and not nodes[i+2]:
            treenode.right = TreeNode(nodes[i+2])
            stack.append(treenode.right)
        if i + 1 < len(nodes) and not nodes[i+1]:
            treenode.left = TreeNode(nodes[i+1])
            stack.append(treenode.left)

