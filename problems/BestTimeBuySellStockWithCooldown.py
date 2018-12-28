class Solution:
    def maxProfit(self, prices):
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

