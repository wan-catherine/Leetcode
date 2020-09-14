"""
dp[i][j] : the maximum length of palindromic subsequence from s[i:j+1]
There are two situations:
    1. s[i] == s[j] ==> dp[i][j] = 2 + dp[i+1][j-1]
    2. s[i] != s[j] ==> dp[i][j] = max(dp[i+1][j], dp[i][j-1])

dp[i][i] = 1 , it only contains one char.
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[0]*length for _ in range(length)]

        for i in range(length - 1):
            dp[i][i] = 1
            dp[i][i+1] = 2 if s[i] == s[i+1] else 1
        dp[-1][-1] = 1

        for l in range(2, length):
            for i in range(length - l):
                j = i + l
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = 2 + dp[i+1][j-1]
        return dp[0][-1]
