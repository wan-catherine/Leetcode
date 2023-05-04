import collections
import sys
from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        freq = [0] * n
        def bfs(start, end):
            visited = set()
            arr = [(start, [start])]
            while arr:
                narr = []
                for node, li in arr:
                    if node == end:
                        return li
                    visited.add(node)
                    for nxt in graph[node]:
                        if nxt in visited:
                            continue
                        narr.append((nxt, li + [nxt]))
                arr = narr

        for s, e in trips:
            li = bfs(s, e)
            for node in li:
                freq[node] += 1

        memo = {}
        def helper(node, parent, can_half):
            if (node, parent, can_half) in memo:
                return memo[(node, parent, can_half)]
            if can_half:
                cost = freq[node] * price[node] // 2
            else:
                cost = freq[node] * price[node]
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                if can_half:
                    ncost = helper(nxt, node, False)
                else:
                    ncost = min(helper(nxt, node, False), helper(nxt, node, True))
                cost += ncost
            memo[(node, parent, can_half)] = cost
            return cost

        res = sys.maxsize
        for node in range(n):
            res = min(res, helper(node, None, False), helper(node, None, True))
        return res