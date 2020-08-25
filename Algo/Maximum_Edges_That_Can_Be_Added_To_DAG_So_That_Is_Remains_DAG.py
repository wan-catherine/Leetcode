import collections
from collections import deque


class Solution:
    def maximumEdgeAddtion(self, num_vertices, connections):
        self.graph = collections.defaultdict(set)
        self.indegree = collections.defaultdict(int)
        self.n = num_vertices

        for u, v in connections:
            self.graph[u].add(v)
            self.indegree[v] += 1

        topological_sort = self.get_topological_sort()
        print(topological_sort)
        res = self.add_edges(topological_sort)
        print(res)

    def add_edges(self, arr):
        res = []
        for i in range(self.n):
            for j in range(i+1, self.n):
                if arr[j] in self.graph[arr[i]]:
                    continue
                res.append((arr[i], arr[j]))
        return res


    def get_topological_sort(self):
        stack = deque([i for i in range(self.n) if i not in self.indegree])
        res = []
        while stack:
            node = stack.popleft()
            res.append(node)
            for i in self.graph[node]:
                self.indegree[i] -= 1
                if self.indegree[i] == 0:
                    stack.append(i)
        return res


solution = Solution()
solution.maximumEdgeAddtion(6, [[5,2], [5,0], [4,0], [4,1], [2,3], [3,1]])