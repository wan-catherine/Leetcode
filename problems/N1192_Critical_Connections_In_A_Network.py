import collections
from typing import List

"""
Classical graph problem : to find the bridge and avoid the SPOF (single point of failure)
Tarjan Algo. 
Use DFS , maintain three arraies : disc, low, parent . 
two kinds of edges here : 
    1. backward edge
    2. cross edge (bridge)
    
"""

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc, low, parent = [-1] * n, [-1] * n, [-1] * n
        res = []
        time = 0
        def dfs(i):
            nonlocal time
            disc[i] = low[i] = time
            time += 1
            for v in graph[i]:
                if v == i:
                    continue
                if disc[v] == -1:
                    parent[v] = i
                    dfs(v)
                    low[i] = min(low[i], low[v])
                    if low[v] > disc[i]:
                        res.append([i, v])
                elif v != parent[i]:
                    low[i] = min(low[i], disc[v])

        for i in range(n):
            if disc[i] == -1:
                dfs(i)
        return res


