from math import inf
"""
d[i][0] = max{d[i-1][0], d[i-1][1] + prices[i]}
d[i][1] = max{d[i-1][1], d[i-2][0] - prices[i]}

here we must use i-1 in d[i][1], because after selling , you need to cooldown one day.
So each time, when you buy a stock, you need to use i - 2.

"""

class Solution:
    def maxProfit_before(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold, sold, rest = float("-inf"), 0 , 0
        for i in prices:
            prevSold = sold
            sold = hold + i
            hold = max(hold, rest - i)
            rest = max(rest, prevSold)
        return max(rest, sold)

    def maxProfit(self, prices):
        d_0 = 0
        d_1 = float(-inf)
        last_sell = 0
        for i in range(0, len(prices)):
            last_d_0 = d_0
            d_0 = max(d_0, d_1 + prices[i])
            d_1 = max(d_1, last_sell - prices[i])
            last_sell = last_d_0
        return d_0
