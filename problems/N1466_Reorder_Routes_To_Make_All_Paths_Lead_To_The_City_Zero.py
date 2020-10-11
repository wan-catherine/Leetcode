import collections


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        roads = set()
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            roads.add((u, v))
        res = 0
        def dfs(n, p):
            nonlocal res
            if (p, n) in roads:
                res += 1

            for i in graph[n]:
                if i == p:
                    continue
                dfs(i, n)

        dfs(0, -1)
        return res


