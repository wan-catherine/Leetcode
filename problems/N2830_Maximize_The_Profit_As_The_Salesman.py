from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        length = len(offers)
        dp = [0] * (n + 1)
        offers.sort(key=lambda x:(x[1],x[0],-x[2])) # sort is the key part
        idx = 0
        for i in range(n):
            dp[i+1] = dp[i]
            while idx < length and i == offers[idx][1]:
                dp[i+1] = max(dp[i+1], offers[idx][2] + dp[offers[idx][0]])
                idx += 1
        return dp[-1]