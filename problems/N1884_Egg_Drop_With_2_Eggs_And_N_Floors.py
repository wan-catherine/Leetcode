class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[n, n] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        # this line is a key!!!
        dp[0][1] = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i][1] = min(dp[i][1], max(dp[j-1][0] + 1, dp[i-j][1] + 1))
        return dp[-1][-1]