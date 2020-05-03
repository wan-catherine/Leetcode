from math import inf


class Solution:
    def maxProfit_before(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) <= 1:
            return 0

        res = 0
        i = 1
        buy = None
        while i < len(prices):
            if prices[i-1] > prices[i]:
                if buy != None and prices[i-1] > buy:
                    res += prices[i-1] - buy
                    buy = None
            else:
                if buy == None and prices[i-1] < prices[i]:
                    buy = prices[i-1]
                if i == len(prices) - 1 and buy != None and buy < prices[-1]:
                    res += prices[i] - buy
            i += 1
        return res

    def maxProfit_better(self, prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i] 

        return max_profit

# i : the ith day
# j : the state of holding stock : 0 or 1 (0 means no stock, 1 means has stock)
# d[i][j] : at the ith day, i have j stock in hand, the profit I get now
#
# d[i][0] is the maximum of those two situation:
#     1. at the (i-1)day, I don't hold stock : d[i-1][0]
#     2. at the (i-1)day, I hold stock and sell one today : d[i-1][1] + price(i)
# d[i][1] is the maximum of those two situation:
#     1. at the (i-1)day, I hold stock : d[i-1][1]
#     2. at the (i-1)day, I don't hold stock and buy one today : d[i-1][0] - price(i)
# d[i][0] = max(d[i-1][0], d[i-1][1] + prices[i])
# d[i][1] = max(d[i-1][1], d[i-1][0] - prices[i])
# at last, return d[len(prices)-1][0]
# why no d[len(prices)-1][1]? becasue sell stock always >= hold the stock at last day
# or you can compare them, and return the larger one , if you want :)

    def maxProfit(self, prices):
        d_0 = 0
        d_1 = float(-inf)
        for i in range(0, len(prices)):
            last_d_0 = d_0
            d_0 = max(d_0, d_1 + prices[i])
            d_1 = max(d_1, last_d_0 - prices[i])
        return d_0



