import collections
import sys
from typing import List

"""
Two Topological sort 
First : 
    remove all useless node 
Second : 
    get the height
    
The we need to access those nodes which height[node] > 2
Because we need to return back the original first access node, so it doesn't matter which node we choose . 
The result is the double of the number of edges we need to access .   

"""
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        length = len(coins)
        graph = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        pq = []
        deleted = [False] * length
        visited = [False] * length
        for i in range(length):
            if degrees[i] == 1 and coins[i] == 0:
                pq.append(i)
                deleted[i] = True
                visited[i] = True

        while pq:
            npq = []
            for idx in pq:
                for nxt in graph[idx]:
                    degrees[nxt] -= 1
                    visited[nxt] = True
                    if degrees[nxt] == 1 and coins[nxt] == 0:
                        npq.append(nxt)
                        deleted[nxt] = True
            pq = npq

        height = [0] * length
        pq = []
        visited = [False] * length
        for i in range(length):
            if degrees[i] == 1 and coins[i] == 1:
                height[i] = 1
                pq.append(i)

        cur = 1
        while pq:
            npq = []
            for idx in pq:
                for nxt in graph[idx]:
                    if deleted[nxt] or visited[nxt]:
                        continue
                    degrees[nxt] -= 1
                    height[nxt] = max(height[nxt], cur + 1)
                    if degrees[nxt] == 1:
                        npq.append(nxt)
                visited[idx] = True
            pq = npq
            cur += 1
        edges = 0
        for i in range(length):
            if height[i] > 2:
                edges += 1
        if edges == 1:
            return 0
        return (edges - 1) * 2







