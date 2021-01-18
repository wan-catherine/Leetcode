import collections
"""
Twice dfs:
first : use any node (a) to search the farest node from a which is b 
second : use b to search the farest node from b which is c 
the answer is the path between b and c

Here we also can use bfs
"""

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        length = len(edges)
        def dfs(node, cur):
            visited[node] = 1
            maxlen, ans = 0, None
            for n in graph[node]:
                if n == node:
                    continue
                if visited[n]:
                    continue
                node, l = dfs(n, cur+1)
                if l > maxlen:
                    maxlen = l
                    ans = node
            if not ans:
                return (node, cur)
            return (ans, maxlen)

        visited = [0] * (length+1)
        left, _ = dfs(0, 0)
        visited = [0] * (length + 1)
        right, res = dfs(left, 0)
        return res


