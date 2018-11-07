class Solution:
    def maxProfit(self, prices):
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


