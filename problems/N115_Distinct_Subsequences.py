class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sl, tl = len(s), len(t)
        s = '#' + s
        t = '#' + t
        dp = [[0]*(tl+1) for _ in range(sl+1)]
        for i in range(sl+1):
            dp[i][0] = 1

        for i in range(1, sl + 1):
            for j in range(1, tl + 1):
                dp[i][j] = dp[i-1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[-1][-1]

