import collections
"""
The key point is convert K into binary .
For example K = 13 = 8 + 4 + 1 = 1101

For ith node , it's 2**j parent == ith node's 2**(j-1) parent, this node's  2**(j-1) parent (parent's parent)
2**j = 2**(j-1) + 2**(j-1)

so for ith node's K == 13 parent, we can find ith node's 8 parent p8, then find p8's 4 parent , p8.4, then p8.4.1.

"""

class TreeAncestor(object):
    # timeout
    # def __init__(self, n, parent):
    #     """
    #     :type n: int
    #     :type parent: List[int]
    #     """
    #     self.node_parents = collections.defaultdict(list)
    #     for i in range(n):
    #         self.node_parents[i].append(parent[i])
    #         if parent[i] in self.node_parents:
    #             self.node_parents[i].extend(self.node_parents[parent[i]])
    #
    #
    # def getKthAncestor(self, node, k):
    #     """
    #     :type node: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     if node not in self.node_parents:
    #         return -1
    #
    #     parents = self.node_parents[node]
    #     if k > len(parents):
    #         return -1
    #     return parents[k-1]

    def __init__(self, n, parent):
        self.ancestor = [[-1] * 20 for _ in range(n)]
        for i in range(n):
            self.ancestor[i][0] = parent[i]
        for i in range(1,20):
            for j in range(n):
                self.ancestor[j][i] = self.ancestor[self.ancestor[j][i-1]][i-1] if self.ancestor[j][i-1] >= 0 else -1


    def getKthAncestor(self, node, k):
        i = self.get_i(k)
        while k > 0:
            node = self.ancestor[node][i]
            k -= 2 ** i
            i = self.get_i(k)
            if node == -1:
                return -1

        return node

    def get_i(self, k):
        i = 0
        while 2 ** (i + 1) <= k:
            i += 1
        return i


if __name__ == "__main__":
    treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    # print(treeAncestor.getKthAncestor(3, 1))
    print(treeAncestor.getKthAncestor(5, 2))
    # print(treeAncestor.getKthAncestor(6, 3))

    treeAncestor = TreeAncestor(10, [-1, 0, 0, 1, 2, 0, 1, 3, 6, 1])
    print(treeAncestor.getKthAncestor(7, 3))