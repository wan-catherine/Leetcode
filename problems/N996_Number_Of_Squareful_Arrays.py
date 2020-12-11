import collections
import math


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        A.sort()
        graph = collections.defaultdict(list)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                val = math.sqrt(A[i] + A[j])
                if int(val) == val:
                    graph[i].append(j)

        visited = [0] * length
        res = 0

        def dfs(i, count):
            nonlocal  res
            if count == length:
                res += 1
            previous = -1
            for j in graph[i]:
                if visited[j] or A[j] == previous:
                    continue
                visited[j] = 1
                previous = A[j]
                dfs(j, count+1)
                visited[j] = 0

        for i in range(length):
            if i and A[i] == A[i-1]:
                continue
            visited[i] = 1
            dfs(i, 1)
            visited[i] = 0

        return res

