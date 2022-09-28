import collections
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        length = len(vals)
        for u, v in edges:
            if vals[u] >= vals[v]:
                graph[u].add(v)
            else:
                graph[v].add(u)
        parent = [i for i in range(length)]
        size = [1] * length

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            if size[pp] >= size[pq]:
                parent[pq] = pp
                size[pp] += size[pq]
            else:
                parent[pp] = pq
                size[pq] += size[pp]

        sv = sorted(set(vals))
        status = collections.defaultdict(set)
        res = 0
        for i, v in enumerate(vals):
            status[v].add(i)
        for v in sv:
            for i in status[v]:
                for j in graph[i]:
                    union(i, j)

            count = collections.Counter()
            for i in status[v]:
                root = find(i)
                count[root] += 1
            for freq in count.values():
                res += freq * (freq - 1) // 2
        return res + length

