class Solution:
    def numberOfWays_TLE(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n + 1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j - 1]
                cur = 1
                for _ in range(x):
                    cur *= j
                if cur <= i:
                    dp[i][j] += dp[i - cur][j - 1]
                dp[i][j] %= MOD
        return dp[-1][-1]

    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, n + 1):
            cur = 1
            for _ in range(x):
                cur *= i

            for j in range(n, 0, -1):
                if j >= cur:
                    dp[j] += dp[j-cur]
                    dp[j] %= MOD
        return dp[n]