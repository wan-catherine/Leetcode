from collections import defaultdict
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(1, n):
            graph[i-1].append(i)

        def bfs(graph):
            stack = set([0])
            step = 0
            while stack:
                nstack = set()
                for i in stack:
                    for j in graph[i]:
                        if j == n - 1:
                            return step + 1
                        nstack.add(j)
                step += 1
                stack = nstack

        res = []
        for i in range(len(queries)):
            u, v = queries[i]
            graph[u].append(v)
            v = bfs(graph)
            if v == 1:
                res.extend([1] * (len(queries) - i))
                break
            res.append(v)
        return res

