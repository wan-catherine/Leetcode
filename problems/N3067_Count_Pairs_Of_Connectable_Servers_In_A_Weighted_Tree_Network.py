from collections import defaultdict
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        length = len(edges) + 1
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = []
        def dfs(parent, node, weight):
            ans = 0
            if weight % signalSpeed == 0:
                ans += 1
            for nxt, w in graph[node]:
                if nxt == parent:
                    continue
                ans += dfs(node, nxt, weight + w)
            return ans

        for i in range(length):
            ans = 0
            prev = 0
            for nxt, w in graph[i]:
                k = dfs(i, nxt, w)
                ans += k * prev
                prev += k
            res.append(ans)
        return res