import collections
import heapq
import math
from collections import deque


class Solution(object):
    def maxProbability_bfs(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph = collections.defaultdict(list)
        for index, li in enumerate(edges):
            graph[li[0]].append((li[1], succProb[index]))
            graph[li[1]].append((li[0], succProb[index]))

        prob = [0]*n
        prob[start] = 1
        stack = deque()
        stack.append(start)

        while stack:
            cur = stack.popleft()
            for i, w in graph[cur]:
                # key point
                if prob[i] >= prob[cur] * w:
                    continue
                prob[i] = prob[cur] * w
                stack.append(i)
        return prob[end]

    """
    Convert it into a Dijkstra : 
    maximum : prob(E1) * prob(E2) * ... * prob(Ek)  ==>
    maximum : log(prob(E1)) + log(prob(E2)) + ... + log(prob(Ek))  ==> here all log(prob(Ek)) < 0 , because prob(Ek) < 1 ==>
    minimum : -log(prob(E1)) - log(prob(E2)) - ... - log(prob(Ek))  ==> a traditional Dijkstra's algo
    """
    def maxProbability(self, n, edges, succProb, start, end):
        graph = collections.defaultdict(list)
        for index, li in enumerate(edges):
            graph[li[0]].append((li[1], -math.log2(succProb[index])))
            graph[li[1]].append((li[0], -math.log2(succProb[index])))

        stack = [(0, start)]
        heapq.heapify(stack)
        final_dist = [-1]*n
        while stack:
            dist, node = heapq.heappop(stack)
            if final_dist[node] != -1:
                continue
            final_dist[node] = dist
            if node == end:
                return 2**(-dist)
            for i, w in graph[node]:
                if final_dist[i] != -1:
                    continue
                heapq.heappush(stack, (final_dist[node] + w, i))
        return 0.0


