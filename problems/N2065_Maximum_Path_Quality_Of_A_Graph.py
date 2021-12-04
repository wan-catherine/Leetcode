import collections
from typing import List

"""
Key point : 
10 <= time(j), maxTime <= 100
which means at most 10 edges we can visit, so just use DFS.
"""
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        length = len(values)
        graph = collections.defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))
        visited = [0] * length
        visited[0] = 1
        res = 0
        def dfs(node, time, count, val):
            nonlocal res
            if count > 10:
                return
            if node == 0:
                res = max(res, val)
            for nxt, t in graph[node]:
                if t > time:
                    continue
                if not visited[node]:
                    val += values[node]
                visited[node] += 1
                dfs(nxt, time-t, count+1, val)
                visited[node] -= 1
                if not visited[node]:
                    val -= values[node]
        dfs(0, maxTime, 0, values[0])
        return res


