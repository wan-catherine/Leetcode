import collections


class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        innodes = set()
        for f, t in edges:
            innodes.add(t)
        res = []
        for i in range(n):
            if i in innodes:
                continue
            res.append(i)
        return res
