from unittest import TestCase
from problems.N2646_Minimize_The_Total_Price_Of_The_Trips import Solution

class TestSolution(TestCase):
    def test_minimum_total_price(self):
        self.assertEqual(23, Solution().minimumTotalPrice(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]))

    def test_minimum_total_price_1(self):
        self.assertEqual(1, Solution().minimumTotalPrice(n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]))
