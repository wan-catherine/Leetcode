import collections
from typing import List

"""
Key point: 
when do '&', the more number involve, the smaller of result is . 
So in order to get minimum cost, we will '&' all edge in the same component.
"""
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parents = [i for i in range(n)]
        sizes = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(p, q):
            if sizes[p] < sizes[q]:
                parents[p] = q
                sizes[q] += sizes[p]
            else:
                parents[q] = p
                sizes[p] += sizes[q]

        for u, v, w in edges:
            p, q = find(u), find(v)
            if p == q:
                continue
            union(p, q)

        status = collections.defaultdict(set)
        for u, v, w in edges:
            p, q = find(u), find(v)
            status[p].add(w)
            status[q].add(w)

        ans = collections.defaultdict(int)
        for k, li in status.items():
            li = list(li)
            ans[k] = li[0]
            for v in li[1:]:
                ans[k] &= v

        res = []
        for u, v in query:
            p, q = find(u), find(v)
            if p != q:
                res.append(-1)
            else:
                res.append(ans[p])
        return res

