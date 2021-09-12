import collections
import heapq
from typing import List

"""
Dijkstra's algorithm

1. use Dijkstra's algo to get from 0 to all nodes's shortest path. 
2. for edge (u,v,w), 0->u, 0->v, to check if the maxMoves can still move to the small nodes between u and v . 
3. for those reachable big node , we need to add them into the results. 
"""
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w+1))
            graph[v].append((u, w+1))
        pq = [(0,0)]
        distances = [0] * n
        visited = [0] * n
        while pq:
            dis, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = 1
            distances[node] = dis
            for nxt, w in graph[node]:
                if dis + w > maxMoves:
                    continue
                if visited[nxt]:
                    continue
                heapq.heappush(pq, (dis + w, nxt))
        res = 0
        # only add the edge's node
        for u, v, w in edges:
            ans = 0
            if visited[u]:
                ans += maxMoves - distances[u]
            if visited[v]:
                ans += maxMoves - distances[v]
            res += min(w, ans)
        # add the node
        for i in range(n):
            if visited[i]:
                res += 1
        return res