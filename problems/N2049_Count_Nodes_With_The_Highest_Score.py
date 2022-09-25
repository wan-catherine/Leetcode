import collections
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        length = len(parents)
        status = [0] * length
        graph = collections.defaultdict(set)
        for i, p in enumerate(parents):
            graph[p].add(i)

        def dfs(node):
            if node not in graph:
                status[node] = 1
                return 1
            val = 1
            for nxt in graph[node]:
                val += dfs(nxt)
            status[node] = val
            return val

        dfs(0)
        res, count = 0, 0
        for i in range(length):
            ans = 1
            ct = status[0] - 1
            for nxt in graph[i]:
                if status[nxt] > 0:
                    ans *= status[nxt]
                    ct -= status[nxt]
            if ct > 0:
                ans *= ct
            if ans > res:
                res = ans
                count = 1
            elif ans == res:
                count += 1
        return count