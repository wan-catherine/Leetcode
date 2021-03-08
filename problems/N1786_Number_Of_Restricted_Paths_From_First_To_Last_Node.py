import collections
import heapq
from typing import List
"""
Dijkstr to get the distanceToLastNode
Then use top-down (dfs + memo) to get the answer.

Key point : 
to understand the requirement : a restricted path is a path with decreasing distanceToLastNode for 1 to n. 
"""

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for u, v, w in edges:
            graph[u].add((v, w))
            graph[v].add((u, w))
        dist = [-1] * (n + 1)
        pr = [(0, n)]
        while pr:
            d, node = heapq.heappop(pr)
            if dist[node] != -1:
                continue
            dist[node] = d
            for nxt, weight in graph[node]:
                if dist[nxt] != -1:
                    continue
                heapq.heappush(pr, (weight+d, nxt))
        memo = {}
        def dfs(index, prev):
            if index == n:
                return 1
            if (index, prev) in memo:
                return memo[(index, prev)]
            cur = 0
            for nxt, _ in graph[index]:
                if dist[nxt] >= prev:
                    continue
                cur += dfs(nxt, dist[nxt])
            memo[(index, prev)] = cur
            return cur
        ans = dfs(1, dist[1])
        return ans % (10**9 + 7)


