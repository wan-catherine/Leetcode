class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        connections = []
        for i in range(length):
            for j in range(i + 1, length):
                # print(i, j)
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                connections.append((dis, i, j))

        connections.sort(key=lambda x: x[0])
        parents = [i for i in range(length)]
        sizes = [1] * length

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(pp, pq):
            if sizes[pp] < sizes[pq]:
                parents[pp] = pq
                sizes[pq] += sizes[pp]
            else:
                parents[pq] = pp
                sizes[pp] += sizes[pq]

        res = 0
        for dis, i, j in connections:
            pi, pj = find(i), find(j)
            if pi == pj:
                continue
            union(pi, pj)
            res += dis

        return res