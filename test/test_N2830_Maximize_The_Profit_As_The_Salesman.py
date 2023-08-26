from unittest import TestCase
from problems.N2830_Maximize_The_Profit_As_The_Salesman import Solution

class TestSolution(TestCase):
    def test_maximize_the_profit(self):
        self.assertEquals(3, Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]))

    def test_maximize_the_profit_1(self):
        self.assertEquals(10, Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]))

    def test_maximize_the_profit_2(self):
        self.assertEquals(17, Solution().maximizeTheProfit(n = 4, offers = [[1,3,10],[1,3,3],[0,0,1],[0,0,7]]))

    def test_maximize_the_profit_3(self):
        self.assertEquals(16, Solution().maximizeTheProfit(n = 4, offers = [[0,0,6],[1,2,8],[0,3,7],[2,2,5],[0,1,5],[2,3,2],[0,2,8],[2,3,10],[0,3,2]]))
