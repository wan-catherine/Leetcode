import collections
from typing import List

"""
Classical graph problem : to find the bridge and avoid the SPOF (single point of failure)
Tarjan Algo. 
Use DFS , maintain three arrays : disc, low, parent . 
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
    """
    We know if there is cycle, the all edges in this cycle won't be the critical connection. 
    So we need to find all edges in the cycle.
    
    Use DFS to traversal the graph, and set it access time/step. 
    and if we find for a node, it can get smaller time/step , then it means the edge inthe cycle. 
    
    """
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        times = [-1] * n
        res = []
        def dfs(t, parent, node):
            times[node] = t + 1
            v = t + 1
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                if times[nxt] == -1:
                    v = min(v, dfs(t+1, node, nxt))
                else:
                    v = min(v, times[nxt])
            if v == t + 1:
                res.append([parent, node])
            times[node] = v
            return v
        dfs(-1, -1, 0)
        return res

