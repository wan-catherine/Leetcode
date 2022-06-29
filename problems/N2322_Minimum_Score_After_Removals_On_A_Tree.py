import collections
import sys
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        sons = collections.defaultdict(set)
        vals = collections.defaultdict(int)
        def dfs(node, parent):
            val = nums[node]
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                val ^= dfs(nxt, node)
                sons[node].update(sons[nxt])
                sons[node].add(nxt)
            vals[node] = val
            return val

        total = dfs(0, -1)
        length = len(nums)
        res = sys.maxsize
        for i in range(1, length):
            for j in range(i+1, length):
                if i == j:
                    continue
                if i in sons[j]:
                    val = [vals[i],  (vals[j] ^ vals[i]), (total ^ vals[j])]
                elif j in sons[i]:
                    val = [vals[j], (vals[i] ^ vals[j]), (total ^ vals[i])]
                else:
                    val = [vals[i], vals[j], (total ^ vals[i] ^ vals[j])]
                val.sort(reverse=True)
                res = min(res, val[0] - val[2])
        return res



