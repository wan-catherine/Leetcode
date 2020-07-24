import collections


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        graphs = collections.defaultdict(list)
        n = len(graph)
        for i in range(n):
            graphs[i].extend(graph[i])

        res = []
        self.dfs(0, [0], res, graphs, n)
        return res

    def dfs(self, node, temp, res, graphs, n):
        if node == n - 1:
            res.append(temp[:])
            return
        for i in graphs[node]:
            temp.append(i)
            self.dfs(i, temp, res, graphs, n)
            temp.pop()

