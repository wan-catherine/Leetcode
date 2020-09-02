"""
Notice, there are N people, so set visited = [False]*n
"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        n = len(M)
        visited = [False]*n
        count = 0
        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 0 or visited[i]:
                    continue
                count += 1
                self.dfs(i, M, n, visited)
        return count

    def dfs(self, index, m, n, visited):
        visited[index] = True
        for i in range(n):
            if visited[i] or not m[index][i]:
                continue
            visited[i] = True
            self.dfs(i, m, n, visited)