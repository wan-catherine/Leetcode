"""
dp[i][j] : sum of a falling path which has i rows,  and end with jth col in the ith row
"""
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = A[0][i]

        for i in range(1, n):
            for j in range(n):
                value = dp[i-1][j]
                if j - 1 >= 0:
                    value = min(value, dp[i-1][j-1])
                if j + 1 < n:
                    value = min(value, dp[i-1][j+1])
                dp[i][j] = value + A[i][j]
        return min(dp[-1])