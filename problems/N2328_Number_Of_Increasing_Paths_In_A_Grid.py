from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        mod = 10 ** 9 + 7

        def dfs(r, c):
            if dp[r][c] > 0:
                return dp[r][c]
            val = 1
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] <= grid[r][c]:
                    continue
                val += dfs(row, col)
                val %= mod
            dp[r][c] = val
            return val

        res = 0
        for i in range(rows):
            for j in range(cols):
                res += dfs(i, j)
                res %= mod
        return res

