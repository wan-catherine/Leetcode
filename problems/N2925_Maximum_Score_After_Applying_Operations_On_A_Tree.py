import collections
from typing import List


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        total = {}
        def dfs(index, parent):
            total[index] = values[index]
            cur = 0
            for nxt in graph[index]:
                if nxt == parent:
                    continue
                cur += dfs(nxt, index)
                total[index] += total[nxt]
            if total[index] == values[index]:
                return 0
            return max(total[index] - values[index], values[index] + cur)
        return dfs(0, -1)
