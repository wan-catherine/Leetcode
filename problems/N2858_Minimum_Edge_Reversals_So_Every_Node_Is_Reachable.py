import collections
from typing import List

"""
Reroot (kind of tree dp)
"""
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 1))
            graph[v].append((u, -1))

        def dfs(cur, parent):
            res = 0
            for nxt, t in graph[cur]:
                if nxt == parent:
                    continue
                if t == -1:
                    res += dfs(nxt, cur) + 1
                else:
                    res += dfs(nxt, cur)
            return res

        res = [0] * n
        count = dfs(0, -1)

        def dfs_check(cur, parent, count):
            res[cur] = count
            for nxt, t in graph[cur]:
                if nxt == parent:
                    continue
                if t == 1:
                    dfs_check(nxt, cur, count + 1)
                else:
                    dfs_check(nxt, cur, count - 1)

        dfs_check(0, -1, count)
        return res
