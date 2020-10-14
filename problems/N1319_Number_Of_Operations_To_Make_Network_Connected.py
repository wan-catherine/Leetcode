import collections


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        length = len(connections)
        if length < n - 1:
            return -1
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in graph[i]:
                dfs(j)

        ans = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            ans += 1
        return ans - 1
