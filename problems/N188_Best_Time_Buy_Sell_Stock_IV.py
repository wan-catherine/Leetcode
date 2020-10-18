import sys
from math import inf

"""
first , consider k 
if k >= len(prices) // 2, then this is same as the 122th in leetcode 
because we can't sell and buy stock at same date, 
the large number of operation(buy and sell is len(prices) // 2

i : the ith day
j : the state of holding stock : 0 or 1 (0 means no stock, 1 means has stock)
d[i][k][j] : at the ith day, I have k operations and have j stock in hand, the profit I get now

d[i][k][0] is the maximum of those two situation:
    1. at the (i-1)day, I don't hold stock and don't do any buy or sell : d[i-1][k][0]
    2. at the (i-1)day, I hold stock and sell one today : d[i-1][k][1] + price(i)
d[i][k][1] is the maximum of those two situation:
    1. at the (i-1)day, I hold stock and don't do any buy or sell : d[i-1][k][1]
    2. at the (i-1)day, I don't hold stock and buy one today : d[i-1][k-1][0] - price(i)
here , buy and sell then means one operation . so you can minus 1 when you buy stock
or can minus 1 when you sell stock .    

d[i][k][0] = max(d[i-1][k][0], d[i-1][k][1] + prices[i])
d[i][k][1] = max(d[i-1][k][1], d[i-1][k-1][0] - prices[i])
at last, return d[len(prices)-1][0]
why no d[len(prices)-1][1]? becasue sell stock always >= hold the stock at last day
or you can compare them, and return the larger one , if you want :)

here about the base case:
when i = 0, i - 1 == -1:
d[-1][*][0] = 0
d[-1][*][1] = float(-inf)

d[0][*][0] = 0
d[0][*][1] = -prices[i]
"""

class Solution:
    def maxProfit_before(self, k, prices):
        n = len(prices)
        if k >= n//2:
            return self.maxProfit_without_k(prices)

        dp_table = [[[0 for i in range(2)] for j in range(k+1)] for p in range(n)]
        print(dp_table)
        for i in range(n):
            for j in range(k,0, -1):
                if i == 0:
                    dp_table[i][j][0] = 0
                    dp_table[i][j][1] = - prices[i]
                    continue
                dp_table[i][j][0] = max(dp_table[i-1][j][0], dp_table[i-1][j][1] + prices[i])
                dp_table[i][j][1] = max(dp_table[i-1][j][1], dp_table[i-1][j-1][0] - prices[i])
        return dp_table[n-1][k][0]

    def maxProfit_without_k(self, prices):
        d_0 = 0
        d_1 = float(-inf)
        for i in range(0, len(prices)):
            last_d_0 = d_0
            d_0 = max(d_0, d_1 + prices[i])
            d_1 = max(d_1, last_d_0 - prices[i])
        return d_0
    """
    Base cases:
    when days = -1, it means it's not even start . so dp[-1][k][0]= 0, dp[-1][k][1] = -infinity means there is no possibility for this case.
    when k = 0, it means we don't even buy/sell, so dp[i][0][0] = 0, dp[i][0][1] = -infinity
    """
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= n // 2:
            return self.maxProfit_without_k(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        for i in range(k + 1):
            dp[-1][i][0], dp[-1][i][1] = 0, -sys.maxsize
        for i in range(n):
            dp[i][0][0], dp[i][0][1] = 0, -sys.maxsize

        for i in range(n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]