import collections


class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, previous):
            res = 0
            for i in graph[node]:
                if i == previous:
                    continue
                flag, count = dfs(i, node)
                if flag:
                    res += count + 2

            if hasApple[node] or res:
                return (True, res)
            return (False, 0)

        flag, ans = dfs(0, -1)
        return ans