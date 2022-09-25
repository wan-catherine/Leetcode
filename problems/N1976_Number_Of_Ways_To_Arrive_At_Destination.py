import collections
import heapq
from typing import List

"""
Dijkstra's algo to get distance[i] : the shortest time from 0 to i. 

then from n-1 to all other nodes which n-1 can directly arrrive , 

"""
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        graph = collections.defaultdict(set)
        for u, v, t in roads:
            graph[u].add((v, t))
            graph[v].add((u, t))
        distance = [-1] * n
        pq = [(0,0)]

        while pq:
            d, node = heapq.heappop(pq)
            if distance[node] >= 0:
                continue
            distance[node] = d
            for nxt, t in graph[node]:
                if distance[nxt] >= 0:
                    continue
                heapq.heappush(pq, (t + d, nxt))
        # print(distance)

        memo = {}
        def dfs(node, d):
            # if distance[node] > d:then there is a path which from 0 - n -1 less than distance[n-1] , impossible .
            # if distance[node] < d: then the node is not the best node we need
            if distance[node] != d:
                return 0
            if node == 0:
                return 1
            if node in memo:
                return memo[node]
            val = 0
            for nxt, t in graph[node]:
                val += dfs(nxt, d - t)
                # val %= MOD
            memo[node] = val
            return val
        return dfs(n-1, distance[-1]) % MOD