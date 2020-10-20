"""
Key point:
when p[j] = '*':
so p[j] can match s[i] ~ s[0], so loop all k from [0,i], if dp[k][j-1] == 1, then it means p[j] matches all chars from s[k+1,i].

But here we can use recursive idea to get rid of loop here :
dp[i][j] = dp[i][j-1] or dp[i-1][j]
    1. dp[i][j-1] : means p[j] == '*' doesn't match any letter
    2. dp[i-1][j] : means p[j] match s[i], then it will can itself to check if p[j] match s[i-1] ans so on
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = '#' + s
        p = '@' + p
        sl, pl = len(s), len(p)
        dp = [[0]*pl for _ in range(sl)]
        dp[0][0] = 1
        for i in range(1, pl):
            if p[i] != '*':
                break
            dp[0][i] = 1

        for i in range(1, sl):
            for j in range(1, pl):
                if p[j] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    # for k in range(i+1):
                    #     if dp[k][j-1] == 1:
                    #         dp[i][j] = 1
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j] == s[i]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

