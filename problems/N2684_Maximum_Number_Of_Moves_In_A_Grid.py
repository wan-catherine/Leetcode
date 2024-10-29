from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            if grid[i][0] < grid[i][1]:
                dp[i][1] = max(dp[i][1], dp[i][0] + 1)
            if i - 1 >= 0 and grid[i - 1][0] < grid[i][1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
            if i + 1 < m and grid[i + 1][0] < grid[i][1]:
                dp[i][1] = max(dp[i][1], dp[i + 1][0] + 1)
            res = max(res, dp[i][1])

        for j in range(2, n):
            for i in range(m):
                if grid[i][j-1] < grid[i][j] and dp[i][j-1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
                if i - 1 >= 0 and grid[i-1][j-1] < grid[i][j] and dp[i-1][j-1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                if i + 1 < m and grid[i+1][j-1] < grid[i][j] and dp[i+1][j-1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 1)
                res = max(res, dp[i][j])
        return res