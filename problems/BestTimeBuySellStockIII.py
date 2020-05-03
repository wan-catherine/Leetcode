from math import inf


class Solution(object):
    def maxProfit_before(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        DP Formular:
        i: Transaction
        j: the jth days
        T[i][j] = max(A, B)
        
        A = T[i][j-1]     we don't do any transact at day j 
        B = T[i-1][m] + prices[j] - prices[m]   we sell at day j , and buy at m , m in (0...j-1)
        
        
        also , we can change B's order :
        B = prices[j] + (T[i-1][m] - prices[m]
        
        Then we can use a variable maxDiff:
        B = prices[j] + maxDiff
        maxDiff = max(maxDiff, T[i-1][j-1] - prices[j-1])
        """
        # if prices == None or len(prices) == 0:
        #     return 0
        #
        # res = [[0 for i in range(len(prices))] for j in range(3)]
        # for i in range(1,3):
        #     maxDiff = res[i][0] - prices[0]
        #     for j in range(1, len(prices)):
        #         maxDiff = max(maxDiff, res[i-1][j-1] - prices[j-1])
        #         res[i][j] = max(res[i][j-1], maxDiff+prices[j])
        # return res[-1][-1]
        return self.maxProfitN(prices, 2)

    def maxProfitN(self, prices, n):
        """
        :type prices: List[int]
        :type n: the most tranaction times
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0

        res = [[0 for i in range(len(prices))] for j in range(n+1)]
        for i in range(1,n+1):
            maxDiff = res[i][0] - prices[0]
            for j in range(1, len(prices)):
                maxDiff = max(maxDiff, res[i-1][j-1] - prices[j-1])
                res[i][j] = max(res[i][j-1], maxDiff+prices[j])
        return res[-1][-1]

    def maxProfit(self, prices):
        d_1_0, d_2_0 = 0, 0
        d_1_1, d_2_1 = float(-inf), float(-inf)
        for i in range(len(prices)):
            d_1_0 = max(d_1_0, d_1_1 + prices[i])
            d_1_1 = max(d_1_1, -prices[i])
            d_2_0 = max(d_2_0, d_2_1 + prices[i])
            d_2_1 = max(d_2_1, d_1_0 - prices[i])
        return d_2_0