from typing import List

"""
unbounded knapsack (repetition of items allowed)
"""

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = ['#' for _ in range(target + 1)]
        dp[0] = ''
        for j in range(1, target + 1):
            for i in range(9):
                if j >= cost[i] and dp[j-cost[i]] != '#':
                    v = dp[j-cost[i]] + str(i+1)
                    if len(v) > len(dp[j]) or (len(v) == len(dp[j]) and v > dp[j]):
                        dp[j] = v
        return dp[-1] if dp[-1] != '#' else '0'





