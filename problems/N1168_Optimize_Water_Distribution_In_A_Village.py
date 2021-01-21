"""
Key point :
add a vitual node : 0 as the water reservoir. The cost it connects to each other village is the cost of building a well.
"""
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        parents = [i for i in range(n+1)]
        sizes = [1] * (n+1)
        # 0 represents water reservior
        for i, c in enumerate(wells):
            pipes.append((0, i+1, c))

        pipes.sort(key=lambda x:x[2])

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
        for u, v, w in pipes:
            p,q = find(u), find(v)
            if p == q:
                continue
            union(p, q)
            res += w
        return res