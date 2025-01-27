import collections
from typing import List


class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        memo = {}
        def bfs(i):
            if i in memo:
                return memo[i]
            stack = set([i])
            ans = set()
            while stack:
                new_stack = set()
                for k in stack:
                    for j in graph[k]:
                        ans.add(j)
                        new_stack.add(j)
                stack = new_stack
            memo[i] = ans
            return memo[i]
        for i in range(n):
            bfs(i)

        res = []
        for i, j in queries:
            if j in memo[i]:
                res.append(True)
            else:
                res.append(False)
        return res

    def checkIfPrerequisite_20250127(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = {}
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)
        def dfs(idx):
            if idx in dp:
                return dp[idx]
            depends = set()
            for nxt in graph[idx]:
                depends.add(nxt)
                depends.update(dfs(nxt))
            dp[idx] = depends
            return depends

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        res = []
        for u, v in queries:
            if u in dp and v in dp[u]:
                res.append(True)
            else:
                res.append(False)
        return res