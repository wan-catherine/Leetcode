import sys

"""
dp[i][j][k] : j houses split into i groups and the jth house paint color k.

"""
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = [[[sys.maxsize] * (n+1) for _ in range(m+1)] for _ in range(target+1)]

        for i in range(n+1):
            dp[0][0][i] = 0

        for i in range(1, target + 1):
            for j in range(i, m+1):
                if houses[j-1] == 0:
                    for k in range(1, n+1):
                        for u in range(1, n+1):
                            if k == u:
                                dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][k] + cost[j-1][k-1])
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][u] + cost[j-1][k-1])
                else:
                    k = houses[j-1]
                    for u in range(1, n+1):
                        if k == u:
                            dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][k])
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][u])
        val = min(dp[-1][-1])
        return -1 if val == sys.maxsize else val

