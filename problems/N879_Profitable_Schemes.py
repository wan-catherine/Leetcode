from typing import List

"""
0-1 Knapsack question. 
dp[i][j][k] : the number of profitable schemes which commit the first i-th crimes and use k person and 
get at least j profit. 

"""

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
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



