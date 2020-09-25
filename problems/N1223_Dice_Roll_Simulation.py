class Solution(object):
    def dieSimulator_tle(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        roll = max(n, max(rollMax)) + 1
        dp = [[[0]*roll for _ in range(7)] for _ in range(n)]
        for i in range(1, 7):
            dp[0][i][1] = 1

        for i in range(1, n):
            for j in range(1, 7):
                for k in range(1, rollMax[j-1]+1):
                    if k > 1:
                        dp[i][j][k] = dp[i-1][j][k-1]
                    else:
                        for p in range(1, 7):
                            if p == j:
                                continue
                            dp[i][j][1] += sum(dp[i-1][p]) % (10**9+7)
        res = 0
        for i in range(1, 7):
            res += sum(dp[-1][i])
        return res % (10**9+7)

    def dieSimulator(self, n, rollMax):
        dp = [[0]*7 for _ in range(n+1)]
        for i in range(6):
            dp[1][i] = 1
        dp[1][-1] = 6

        for i in range(2, n+1):
            for j, val in enumerate(rollMax):
                dp[i][j] = dp[i-1][-1]
                if val + 1 < i:
                    dp[i][j] -= dp[i-val-1][-1] - dp[i-val-1][j]
                elif val + 1 == i:
                    dp[i][j] -= 1
                dp[i][-1] = sum(dp[i][:6]) % (10**9+7)
        return dp[-1][-1] % (10**9+7)

