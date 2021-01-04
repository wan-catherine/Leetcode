"""
There are two situations :
    1. the redundant edge connects to root
        then all vertice will have 1 indegree
    2. the redundant edge doesn't connect to root
        then there is one vertice have 2 indegrees which means one of its edge is the answer.
        But we can't randomly delete one of them. We need to keep the one from root / sibling to it . and
        delete the one from it's children to it .
"""
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parents = [i for i in range(n+1)]
        candidates = []
        for u, v in edges:
            if parents[v] == v:
                parents[v] = u
            else:
                candidates.append([u, v])
                candidates.append([parents[v], v])
                break

        def find(p):
            while p != parents[p]:
                p = parents[p]
            return p

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            parents[pq] = pp

        def connected(p, q):
            return find(p) == find(q)

        parents = [i for i in range(n+1)]
        for u, v in edges:
            if candidates:
                if [u, v] == candidates[0]:
                    continue
                if connected(u, v):
                    return candidates[1]
                union(u, v)
            else:
                if connected(u, v):
                    return [u, v]
                union(u, v)
        return candidates[0]

