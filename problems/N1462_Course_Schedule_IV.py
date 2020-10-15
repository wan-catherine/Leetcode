import collections


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