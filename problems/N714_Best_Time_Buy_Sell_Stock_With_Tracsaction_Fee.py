from math import inf
"""
smiliar as 122
d[i][0] = max(d[i-1][0], d[i-1][1] + prices[i])
d[i][1] = max(d[i-1][1], d[i-1][0] - prices[i] - fee)
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        d_0 = 0
        d_1 = float(-inf)
        for i in range(0, len(prices)):
            last_d_0 = d_0
            d_0 = max(d_0, d_1 + prices[i])
            d_1 = max(d_1, last_d_0 - prices[i] - fee)
        return d_0