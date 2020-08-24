# Definition for a undirected graph node
class Node:
    def __init__(self, x):
        self.val = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        created = {}
        return self.helper(node, created)

    def helper(self, node, created):
        if node.val not in created:
            new_node = Node(node.val)
            created[node.val] = new_node
        else:
            new_node = created[node.val]
        neighbors = node.neighbors
        new_neighbors = []
        for i in neighbors:
            if i.val in created:
                new_neighbors.append(created[i.val])
            else:
                new_neighbors.append(self.helper(i, created))
        new_node.neighbors = new_neighbors
        return new_node