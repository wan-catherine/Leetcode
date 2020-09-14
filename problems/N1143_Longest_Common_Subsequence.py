"""
dp[i][j] means the length of longest common subsequence for text1[:i+1] and text2[:j+1]
    1. text1[i] == text2[j] ==> dp[i][j] = 1 + dp[i-1][j-1]
    2. text1[i] != text2[j] ==> dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        rows, cols = len(text1), len(text2)
        dp = [[0] * cols for _ in range(rows)]

        flag = False
        for i in range(rows):
            if text1[i] != text2[0] and not flag:
                dp[i][0] = 0
            else:
                flag = True
                dp[i][0] = 1
        flag = False
        for i in range(cols):
            if text1[0] != text2[i] and not flag:
                dp[0][i] = 0
            else:
                flag = True
                dp[0][i] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]