import collections
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        length = len(patience)
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        steps = [sys.maxsize] * length
        stack = [(0, 0)]
        visited = set([0])
        while stack:
            nstack = []
            for i, t in stack:
                steps[i] = t
                for nxt in graph[i]:
                    if nxt in visited:
                        continue
                    nstack.append((nxt, t + 1))
                    visited.add(nxt)
            stack = nstack
        ans = 0

        for i in range(1, length):
            c, p = steps[i] * 2, patience[i]
            if c < p:
                ans = max(ans, c + 1)
            else:
                t = (c - 1) // p * p  # here we need to minus one, because the second starts from 0
                ans = max(ans, t + c + 1)
        return ans