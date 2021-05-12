class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(arrLen, steps//2+2)
        dp = [[0] * n for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1, steps+1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
                elif j == n - 1:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        return dp[steps][0] % (10**9+7)