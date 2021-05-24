"""
circular permutation
stirling number.

We can think this way, we need to split n numbers into k groups, each group is a circular permutation.

choosing m from n numbers to construct a permutation:
A(n, m) = n! / (n - m)!

choosing m from n numbers to construct a circular permutation:
H(n, m) = n! / (n - m)! / m

using n numbers to construct m circular permutation:
dp[i][j] : the number of ways that we can use the first i numbers to construct j circular permutations.
Two situations :
    1. if i-th element is for a new circular permuation: dp[i-1][j-1]
    2. if i-th element is the part of the existed circular permuation,
    then insert it to the previous j circular permutations : dp[i-1][j] * (i-1)

    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * (i - 1)
"""
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, min(k, n) + 1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * (i-1)
        return dp[n][k] % (10**9+7)
