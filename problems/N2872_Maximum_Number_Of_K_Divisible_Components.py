import collections
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(parent, node):
            ans = 0
            tl = 0
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                count, left = dfs(node, nxt)
                ans += count
                tl += left
            if (tl + values[node]) % k == 0:
                return (ans + 1, 0)
            else:
                return (ans, tl + values[node])

        res, l = dfs(-1, 0)
        return res