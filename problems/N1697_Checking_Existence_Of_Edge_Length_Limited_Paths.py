"""
Union-Find problem.
If we only have one query, then we can use normal union-find to check.
The time complexity is O(E).
If we check all query by this way it will be O(E**2), TLE.

Key point :
For each query, we can only add those distance of the edge which strictly less than the query's limitation.
So we can make sure all edgeList just add/check by once.
"""
class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parents = [i for i in range(n)]
        sizes = [1 for _ in range(n)]

        def find(x):
            while parents[x] != parents[parents[x]]:
                x = parents[x]
            return parents[x]

        def union(p, q):
            rp, rq = find(p), find(q)
            if rp == rq:
                return
            if sizes[rp] > sizes[rq]:
                parents[rq] = rp
                sizes[rp] += sizes[rq]
            else:
                parents[rp] = rq
                sizes[rq] += sizes[rp]
        l = len(queries)
        for i in range(l):
            queries[i].append(i)

        edgeList.sort(key=lambda x:x[2])
        queries.sort(key=lambda x:x[2])

        res = [True]*l
        length = len(edgeList)
        i = 0
        for li in queries:
            while i < length and edgeList[i][2] < li[2]:
                union(edgeList[i][0], edgeList[i][1])
                i+= 1
            if find(li[0]) != find(li[1]):
                res[li[3]] = False
        return res






