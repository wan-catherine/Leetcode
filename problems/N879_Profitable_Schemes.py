from typing import List

"""
0-1 Knapsack question. 
dp[i][j][k] : the number of profitable schemes which commit the first i-th crimes and use k person and 
get at least j profit. 

"""

class Solution:
    def profitableSchemes_(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        profit = [0] + profit
        group = [0] + group
        length = len(profit)
        dp = [[[0]* (n + 1) for _ in range(minProfit+1)] for _ in range(length)]
        dp[0][0][0] = 1

        for i in range(1, length):
            p, g = profit[i], group[i]
            for j in range(minProfit+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if k >= g:
                        v = max(0, j - p)  # if the current crime's profit is super large , then v = 0.
                        dp[i][j][k] += dp[i-1][v][k-g]
        return sum(dp[-1][-1]) % (10**9+7)

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n+1)]
        dp[0][0] = 1
        length = len(group)
        for k in range(length):
            dp_new = [li[:] for li in dp]
            for i in range(n+1):
                for j in range(minProfit+1):
                    if group[k] + i <= n:
                        val = min(j + profit[k], minProfit)
                        dp_new[i+group[k]][val] += dp[i][j]
            dp = dp_new
        res = 0
        for i in range(n+1):
            res += dp[i][minProfit]
        return res % (10**9+7)


