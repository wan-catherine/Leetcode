import collections
from typing import List


class Solution(object):
    def findMinHeightTrees_n_n_timeout(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.n = n
        if not edges:
            return [n-1]
        self.graph = collections.defaultdict(set)
        for u, v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)

        height = self.n
        res = []
        for i in range(n):
            self.visited = set()
            h = self.bfs(i)
            if h < height:
                height = h
                res = [i]
            elif h == height:
                if res:
                    res.append(i)
                else:
                    res = [i]

        return res

    def bfs(self, v):
        h = 0
        stack = [v]
        while stack:
            h += 1
            new_stack = []
            for i in stack:
                self.visited.add(i)
                for j in self.graph[i]:
                    if j not in self.visited:
                        new_stack.append(j)
            stack = new_stack
        return h

    """
    delete leaves one layer by one layer. 
    after delete the first layer of leaves , then need to update the next layer's graph. 
    len(graph[i]) == 1 means i is leaf
    """
    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [0]
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            indegree[u] += 1
            indegree[v] += 1

        stack = [i for i, j in indegree.items() if j == 1]
        nodes = set([i for i in range(n)])
        while len(nodes) > 2:
            new_stack = []
            for i in stack:
                nodes.remove(i)
                for j in graph[i]:
                    graph[j].remove(i)
                    if len(graph[j]) == 1:  #this is the key part . We only delete leaves.
                        new_stack.append(j)
            stack = new_stack
        return list(nodes)

    def findMinHeightTrees_20220803(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            indegree[v] += 1
            indegree[u] += 1

        leaves = [i for i in indegree if indegree[i] == 1]
        nodes = set([i for i in range(n)])
        while len(nodes) > 2:
            nleaves = []
            for node in leaves:
                nodes.remove(node)
                for nxt in graph[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 1:
                        nleaves.append(nxt)
            leaves = nleaves
        return list(nodes)
