import sys

"""
Classical interval range DP
key point : in order to avoid wrapping issue, choose the start and end index : A[0], A[length-1] as the base line. 
Notice , any of the two points are one of the side of the triangle.
We have two points, then choose the third one from the left points. Here we need to do loop as k . 

When there are only three points , then dp[i][k] + dp[k][j] + A[i]*A[k]*A[j] == A[i]*A[k]*A[j] ==>
the base condition : dp[i-1][i] = 0

Another key point, for the range , it can be from [2, length] inclusive. 
"""

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        dp = [[sys.maxsize] * length for _ in range(length)]
        for i in range(1, length):
            dp[i-1][i] = 0

        for l in range(2, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
        return dp[0][-1]
