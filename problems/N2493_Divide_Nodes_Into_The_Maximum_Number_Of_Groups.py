import collections
from typing import List

"""
Key points:
1. the root can only has one node . if have more : 
a, b -> c -> ...
is no better than : 
a -> c -> b 
"""

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        status = collections.defaultdict(int)
        for start in range(1,n+1):
            stack = [(start, 1)]
            sid = start
            levels = [0] * (n + 1)
            levels[start] = 1
            current = 1
            while stack:
                nstack = []
                for i, l in stack:
                    for nxt in graph[i]:
                        if levels[nxt] == l:
                            return -1
                        if levels[nxt] != 0:
                            continue
                        levels[nxt] = l + 1
                        nstack.append((nxt, l + 1))
                        sid = min(sid, nxt)
                stack = nstack
                if stack:
                    current = l + 1
            status[sid] = max(status[sid], current)
        for k, v in status.items():
            res += v
        return res
