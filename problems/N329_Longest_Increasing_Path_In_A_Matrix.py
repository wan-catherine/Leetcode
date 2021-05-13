import collections
from typing import List


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(matrix), len(matrix[0])
        graph = collections.defaultdict(set)
        indegrees = [[0]*cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                for i, j in directions:
                    r, c = row + i, col + j
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue
                    if matrix[r][c] < matrix[row][col]:
                        indegrees[row][col] += 1
                        graph[(r, c)].add((row, col))

        zero_ingrees = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if not indegrees[row][col]:
                    zero_ingrees.append((row, col))

        # topological sort , smiliar as BFS
        while zero_ingrees:
            res += 1
            for _ in range(len(zero_ingrees)):
                row, col = zero_ingrees.popleft()
                for i, j in graph[(row, col)]:
                    indegrees[i][j] -= 1
                    if not indegrees[i][j]:
                        zero_ingrees.append((i,j))
        return res

    """
    here memo[(i,j)] mens the longest increasing path which starts from matrix[i][j]
    """
    def longestIncreasingPath_dfs(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            ans = 1
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] <= matrix[r][c] :
                    continue
                ans = max(ans, dfs(row, col) + 1)
            memo[(r,c)] = ans
            return ans

        for i in range(rows):
            for j in range(cols):
                ans = dfs(i, j)
                res = max(res, ans)
        return res