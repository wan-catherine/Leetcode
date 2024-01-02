from collections import defaultdict
from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        memo = {}
        def dfs(node, parent, times):
            if times > 13:
                times = 13
            if (node, times) in memo:
                return memo[(node, times)]
            cur = coins[node] // (2 ** times)
            tf = cur - k
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                tf += dfs(nxt, node, times)
            sf = cur // 2
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                sf += dfs(nxt, node, times + 1)
            memo[(node, times)] = max(tf, sf)
            return memo[(node, times)]

        return dfs(0, -1, 0)
