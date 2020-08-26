import collections
class Solution:
    def longestCable(self, n, connections):
        self.graph = collections.defaultdict(set)
        self.len_map = collections.defaultdict(int)
        for u, v, l in connections:
            self.graph[u].add(v)
            self.graph[v].add(u)
            self.len_map[(u,v)] = l
            self.len_map[(v,u)] = l
        res = 0
        for i in range(1, n+1):
            self.visited = set()
            res = max(res, self.dfs(i, 0))
        return res

    def dfs(self, node, length):
        self.visited.add(node)
        h = length
        for next in self.graph[node]:
            if next in self.visited:
                continue
            length = max(length, self.dfs(next, self.len_map[(node,next)] + h))
        return length

solution = Solution()
res = solution.longestCable(6, [(1,2,3),(2,3,4),(2,6,2),(6,4,6),(6,5,5)])
print(res)