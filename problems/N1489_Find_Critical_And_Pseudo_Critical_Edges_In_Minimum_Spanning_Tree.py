import sys

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, li in enumerate(edges):
            li.append(i)
        edges.sort(key = lambda x : x[2])

        def kruskal(index, edge):
            nonlocal n
            parents = [i for i in range(n)]
            sizes = [1] * n

            def find(x):
                while x != parents[x]:
                    parents[x] = parents[parents[x]]
                    x = parents[x]
                return x

            def union(p, q):
                if sizes[p] < sizes[q]:
                    parents[p] = q
                    sizes[q] += sizes[p]
                else:
                    parents[q] = p
                    sizes[p] += sizes[q]

            res = 0
            if edge:
                p, q = find(edge[0]), find(edge[1])
                if p != q:
                    union(p, q)
                    res += edge[2]

            for u, v, w, i in edges:
                if i == index:
                    continue
                p, q = find(u), find(v)
                if p == q:
                    continue
                union(p, q)
                res += w
            # sometimes, when you remove some edge, it won't get the MST.
            for i in range(n):
                parents[i] = find(parents[i])

            return res if len(set(parents)) == 1 else sys.maxsize

        base = kruskal(-1, None)

        critical, pseudo = set(), set()
        for u, v, w, i in edges:
             if base < kruskal(i, None):
                 critical.add(i)

        for u, v, w, i in edges:
            if i in critical:
                continue
            if base == kruskal(-1, (u, v, w, i)):
                pseudo.add(i)

        return [list(critical), list(pseudo)]

