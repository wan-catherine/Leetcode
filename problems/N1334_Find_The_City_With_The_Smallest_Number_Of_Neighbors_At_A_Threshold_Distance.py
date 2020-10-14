import sys
"""
Floyd Warshall Algo for all pairs shortest path
"""

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        graph = [[sys.maxsize]*n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if i == k or j == k:
                        continue
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        ans = n
        for i in range(n):
            length = len([path for path in graph[i] if path <= distanceThreshold]) - 1
            if length <= ans:
                res = i
                ans = length
        return res


