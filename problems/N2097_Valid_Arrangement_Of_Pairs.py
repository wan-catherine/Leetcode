import collections
from collections import Counter
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indegree, outdegree = collections.defaultdict(int), collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            indegree[b] += 1
            outdegree[a] += 1
        start = -1
        for p in graph.keys():
            if outdegree[p] - indegree[p] == 1:
                start = p
                break
        if start == -1:
            start = pairs[0][0]

        def dfs(point, path):
            while(len(graph[point]) > 0):
                npoint = graph[point].pop()
                dfs(npoint, path)
            path.append(point)

        path = []
        dfs(start, path)
        res = []
        for i in range(len(path)-1, 0, -1):
            res.append([path[i], path[i-1]])
        return res
