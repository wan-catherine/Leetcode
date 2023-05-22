import collections
import sys
from typing import List

"""
Check the shortest cycle, we can just check each edges. 
Remove this edge (u, v) , and use BFS to see the shortest path for (u, v)
the len(path) + 1 == shortest cycle length
"""

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def helper(u, v):
            stack = [(u, v)]
            step = 0
            flag = False
            while stack:
                nstack = []
                for node, parent in stack:
                    for nxt in graph[node]:
                        if nxt == parent :
                            continue
                        if nxt == v:
                            flag = True
                        nstack.append((nxt,node))
                step += 1
                stack = nstack
                if flag:
                    return step + 1
            return -1

        res = sys.maxsize
        for u, v in edges:
            ans = helper(u, v)
            if ans == -1:
                continue
            res = min(res, ans)
            # add this to reduce the useless calculation
            if res == 3:
                return 3
        return -1 if res == sys.maxsize else res