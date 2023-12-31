import collections
from collections import defaultdict
from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        length = len(edges)
        res = [1] * (length + 1)
        mapping = collections.defaultdict(list)
        def dfs(parent, node):
            arr = []
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(node, child)
                for nxt in mapping[child]:
                    arr.append(nxt)
            arr.append(cost[node])
            arr.sort()
            n = len(arr)
            if n < 3:
                res[node] = 1
            else:
                res[node] = max(0, arr[0]*arr[1]*arr[-1], arr[-3]*arr[-2]*arr[-1])

            if n >= 1:
                mapping[node].append(arr[0])
            if n >= 2:
                mapping[node].append(arr[1])
            if n >= 5:
                mapping[node].append(arr[-3])
            if n >= 4:
                mapping[node].append(arr[-2])
            if n >= 3:
                mapping[node].append(arr[-1])

        dfs(-1, 0)
        return res

