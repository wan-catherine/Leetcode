"""
https://www.youtube.com/watch?v=S-fUTfqrdq8
There are three situations.
"""
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[0,0] for _ in range(N+1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for i in range(2, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]
            dp[i][1] = dp[i-2][0] + dp[i-1][1]
        return dp[-1][0] % (10**9 + 7)