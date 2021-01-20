class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        parents = [i for i in range(N+1)]
        sizes = [1] * (N+1)
        res = 0
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

        connections.sort(key = lambda x : x[2])

        for u, v, w in connections:
            p, q = find(u), find(v)
            if p == q:
                continue
            union(p, q)
            res += w

        for i in range(1, N+1):
            parents[i] = find(parents[i])

        if len(set(parents[1:])) > 1:
            return -1
        return res



