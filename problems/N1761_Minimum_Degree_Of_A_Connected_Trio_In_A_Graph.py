import collections
import sys

"""
first I tried to use graph = collections.defaultdict(set), but TLE, 
Then change it to matrix, pass!
"""
class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[0]*(n+1) for _ in range(n+1)]
        degree = collections.defaultdict(int)
        for u, v in edges:
            graph[u][v] = True
            graph[v][u] = True
            degree[u] += 1
            degree[v] += 1
        res = sys.maxsize

        for u in range(1, n+1):
            for v in range(u+1, n+1):
                if not graph[u][v]:
                    continue
                for w in range(v+1, n+1):
                    if not graph[u][w] or not graph[v][w]:
                        continue
                    count = degree[u] + degree[v] + degree[w] - 6
                    res = min(count, res)
        return res if res != sys.maxsize else -1
