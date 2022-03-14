import heapq
import sys
from typing import List

"""
This is the variant Dijkstra's algo . 

Here are three points , so must be three subpath. 
So we use Dijkstra's algo to get all those three path's shortest path and sum up.
"""

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graphnxt, graphprev = [[] for _ in range(n)], [[] for _ in range(n)]
        for u, v, w in edges:
            graphnxt[u].append((v, w))
            graphprev[v].append((u, w))

        def dijkstra(start, graph):
            pq = [(0, start)]
            res = [sys.maxsize] * n
            while pq:
                weight, node = heapq.heappop(pq)
                if res[node] < sys.maxsize:
                    continue
                res[node] = weight
                for nxt, w in graph[node]:
                    if res[nxt] < sys.maxsize:
                        continue
                    heapq.heappush(pq, (weight + w, nxt))
            return res

        dist21 = dijkstra(src1, graphnxt)
        dist22 = dijkstra(src2, graphnxt)
        dist = dijkstra(dest, graphprev)
        res = sys.maxsize
        for i in range(n):
            res = min(res, dist21[i] + dist22[i] + dist[i])
        if res < sys.maxsize:
            return res
        return -1
