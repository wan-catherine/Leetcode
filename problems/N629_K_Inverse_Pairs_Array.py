"""
DP problem. Usually , if it says the answer should be modulo 10**9 + 7, it should be a DP problem.

dp[i][j] : 1 ~ i has j inverse pairs.

xxxxx (i-1 numbers here), then we add ith. it can be :
ixxxxx, so it will add i-1 inverse pairs.
xixxxx, so it will add i-2 inverse pairs.
...
xxxxxi, so it will add i-1 - (i-1) == 0 inverse pairs.
==>
    dp[i][j] = dp[i-1][j-(i-1)] + dp[i-1][j-(i-2)] + ... + dp[i-1][j-1] + dp[i-1][j]
If we directly use this formula , then it will be three level loops.
Here we need to consider math method :
    dp[i][j-1] = dp[i-1][j-1-(i-1)] + dp[i-1][j-1-(i-2)] + ... + dp[i-1][j-1-1] + dp[i-1][j-1] ==>
    dp[i][j-1] = dp[i-1][j-i] + dp[i-1][j-(i-1)] + ... + dp[i-1][j-2] + dp[i-1][j-1]

==> dp[i][j] = dp[i-1][j-(i-1)] + dp[i-1][j-(i-2)] + ... + dp[i-1][j-1] + dp[i-1][j]  a
    dp[i][j-1] = dp[i-1][j-i] + dp[i-1][j-(i-1)] + ... + dp[i-1][j-2] + dp[i-1][j-1]  b

    a - b ==>
    dp[i][j] - dp[i][j-1] = dp[i-1][j] - dp[i-1][j-i]
    ==> dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i] (here we need to make sure j >= i)
"""
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - (dp[i-1][j-i] if j>=i else 0)

        return dp[-1][-1] % (10**9 + 7)
