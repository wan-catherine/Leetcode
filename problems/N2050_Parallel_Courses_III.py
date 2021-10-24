import collections
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [0] * (n + 1)
        pre = collections.defaultdict(list)
        for u, v in relations:
            graph[v] += 1
            pre[u].append(v)
        zero = [(i, time[i-1]) for i in range(1, n + 1) if graph[i] == 0]
        vals = [0] * (n + 1)
        res = 0
        while zero:
            new_zero = []
            for course, t in zero:
                for nxt in pre[course]:
                    graph[nxt] -= 1
                    vals[nxt] = max(vals[nxt], t + time[nxt-1])
                    if graph[nxt] == 0:
                        new_zero.append((nxt, vals[nxt]))
                res = max(res, t)
            zero = new_zero
        return res