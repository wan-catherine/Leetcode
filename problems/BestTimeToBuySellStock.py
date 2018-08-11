class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0

        minValue = prices[0]
        res = [0] * length
        for i in range(1, length):
            minValue = minValue if minValue < prices[i] else prices[i]
            res[i] = res[i - 1] if res[i - 1] > (prices[i] - minValue) else (prices[i] - minValue)
        return res[length - 1]