import bisect
import collections
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        status = collections.defaultdict(list)
        f, s = len(edges1) + 1, len(edges2) + 1
        if k == 0:
            return [1] * f
        fg, sg = collections.defaultdict(list), collections.defaultdict(list)
        for u, v in edges1:
            fg[u].append(v)
            fg[v].append(u)
        for u, v in edges2:
            sg[u].append(v)
            sg[v].append(u)

        for i in range(s):
            now = [0] * s
            nodes = [(i, -1, 0)]
            while nodes:
                nnodes = []
                for cur, parent, level in nodes:
                    now[level] += 1
                    for nxt in sg[cur]:
                        if nxt == parent:
                            continue
                        nnodes.append((nxt, cur, level + 1))
                nodes = nnodes
            bisect.insort_left(status[0], now[0])
            for j in range(1, s):
                now[j] += now[j - 1]
                bisect.insort_left(status[j], now[j])

        res = []
        for i in range(f):
            nodes = [(i, -1, 0)]
            ans = 0
            while nodes:
                nnodes = []
                for cur, parent, level in nodes:
                    ans += 1
                    if level == k:
                        continue
                    for nxt in fg[cur]:
                        if nxt == parent:
                            continue
                        nnodes.append((nxt, cur, level + 1))
                nodes = nnodes

            res.append(ans + (status[k-1][-1] if k <= s else status[s-1][-1]))
        return res
