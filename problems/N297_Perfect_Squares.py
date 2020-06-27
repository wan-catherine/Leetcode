"""
DP
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(2,n+1):
            j = 1
            while (j+1)*(j+1) < i:
                j += 1
            if (j+1)**2 == i:
                dp[i] = 1
                continue
            minimum = i
            while j > 0:
                minimum = min(minimum, dp[i-j**2]+1)
                j -= 1
            dp[i] = minimum
        return dp[-1]
