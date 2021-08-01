import collections
import heapq
from typing import List

"""
Dijkstra Algo
"""

class Solution(object):
    def networkDelayTime_(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        length = len(times)
        if length < N - 1:
            return -1

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        self.dist = [6001] * (N+1)
        self.dist[K] = 0

        self.spt = [False] * (N+1)
        for _ in range(N):
            node = self.find_minimum_node()
            self.spt[node] = True
            if node not in graph:
                continue
            for v, w in graph[node]:
                self.dist[v] = min(self.dist[v], self.dist[node] + w)
        res = max(self.dist[1:])
        return res if res < 6001 else -1

    def find_minimum_node(self):
        minimum = 6001
        res = -1
        for i, val in enumerate(self.dist):
            if not self.spt[i] and val < minimum:
                minimum = val
                res = i
        return res

    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(set)
        for u, v, w in times:
            graph[u].add((w, v))

        pq = [(0, k)]
        visited = [0]*(n+1)
        res = 0
        while pq:
            w, node = heapq.heappop(pq)
            if visited[node]:
                continue
            res = max(res, w)
            visited[node] = 1
            for wgh, nxt in graph[node]:
                heapq.heappush(pq, (wgh+w, nxt))
        return res if sum(visited)==n else -1

    # update at 20210801
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        used = {k: 0}
        stack = [k]
        while stack:
            new_stack = []
            for cur in stack:
                for nxt, t in graph[cur]:
                    if nxt not in used or used[nxt] > used[cur] + t:
                        used[nxt] = used[cur] + t
                        new_stack.append(nxt)
            stack = new_stack
        return max(used.values()) if len(used) == n else -1

