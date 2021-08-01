import collections
from typing import List

from problems.Utility_Tree import TreeNode


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        val_root = collections.defaultdict(TreeNode)
        val_not_root = collections.defaultdict(TreeNode)
        node_parent = collections.defaultdict(TreeNode)
        def get_not_root(parent, node):
            if node:
                node_parent[node] = parent
                val_not_root[node.val] = node
                get_not_root(node, node.left)
                get_not_root(node, node.right)

        for root in trees:
            val_root[root.val] = root
            get_not_root(root, root.left)
            get_not_root(root, root.right)

        sroots = set(val_root.keys())
        snot_roots = set(val_not_root.keys())
        sr = list(sroots.difference(snot_roots))
        if len(sr) != 1:
            return None
        root = val_root[sr[0]]
        count = 1
        def build(node, mm, mx):
            nonlocal count
            if not node:
                return True
            if node.val < mm or node.val > mx:
                return False
            if not node.left and not node.right:
                if node.val not in val_root:
                    return True
                if node in node_parent:
                    parent = node_parent[node]
                    if parent.left == node:
                        parent.left = val_root[node.val]
                    else:
                        parent.right = val_root[node.val]
                    count += 1
                node = val_root[node.val]
            return build(node.left, mm, node.val - 1) and build(node.right, node.val + 1, mx)

        if build(root, 1, 50000) and count == len(val_root):
            return root
        else:
            return None