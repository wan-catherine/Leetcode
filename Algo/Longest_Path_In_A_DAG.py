import collections
from math import inf

"""
For a DAG, find a node: s to all other nodes' longest path. 
1. create topological sort 
2. initialize distances array : distances = [-INF,...,-INF], and distances[s] = 0
3. check all vertex u in topological sort:
    if distances[v] < distances[u] + self.edge_map[(u,v)]: 
        distances[v] = distances[u] + self.edge_map[(u,v)]
4. distances is what we want
"""

class Solution:
    def create_graph(self, n, connections):
        self.n = n
        self.graph = collections.defaultdict(set)
        self.indegree = collections.defaultdict(int)
        self.edge_w_map = collections.defaultdict(int)
        for u, v, w in connections:
            self.graph[u].add(v)
            self.indegree[v] += 1
            self.edge_w_map[(u,v)] = w

    def get_topological_sort(self):
        res = []
        stack = [i for i in range(self.n) if i not in self.indegree]
        visited = set()
        while stack:
            node = stack.pop()
            res.append(node)
            visited.add(node)
            for i in self.graph[node]:
                if i in visited:
                    continue
                self.indegree[i] -= 1
                if not self.indegree[i]:
                    stack.append(i)
        return res

    def longestPath(self, s):
        arr = self.get_topological_sort()
        distances = [float(-inf)] * self.n
        distances[s] = 0

        for i in arr:
            for next in self.graph[i]:
                if distances[next] < distances[i] + self.edge_w_map[(i,next)]:
                    distances[next] = distances[i] + self.edge_w_map[(i,next)]
        print(distances)

solution = Solution()
solution.create_graph(6, [(0, 1, 5),(0,2,3),(1,3,6),(1,2,2),(2,4,4),(2,5,2),(2,3,7),(3,5,1),(3,4,-1),(4,5,-2)])
solution.longestPath(1)