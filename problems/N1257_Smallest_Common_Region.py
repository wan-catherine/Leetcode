import collections

class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        parent = collections.defaultdict(str)
        graph = collections.defaultdict(set)
        points = set()
        for li in regions:
            points.update(set(li))
            for r in li[1:]:
                parent[r] = li[0]
                graph[li[0]].add(r)

        roots = list(points.difference(set(parent.keys())))

        def helper(node, p, q):
            if node == p or node == q:
                return 1, node
            count = 0
            res = []
            for next in graph[node]:
                c, r = helper(next, p, q)
                if c == 2:
                    return c, r
                if c > 0:
                    count += c
                    res.append(r)
            if count == 0:
                return 0, None
            if count == 1:
                return 1, res[0]
            return 2, node

        _, res = helper(roots[0], region1, region2)
        return res