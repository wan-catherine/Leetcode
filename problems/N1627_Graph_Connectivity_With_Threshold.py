class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parents = [i for i in range(n+1)]
        sizes = [1] * (n+1)

        def find(p):
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def union(p, q):
            pp = find(p)
            pq = find(q)
            if pp == pq:
                return
            if sizes[pp] < sizes[pq]:
                parents[pp] = pq
                sizes[pq] += sizes[pp]
            else:
                parents[pq] = pp
                sizes[pp] += sizes[pq]

        for i in range(threshold+1, n+1):
            for j in range(i*2, n+1, i):
                union(i, j)

        res = []
        for u, v in queries:
            if find(u) == find(v):
                res.append(True)
            else:
                res.append(False)
        return res
