from unittest import TestCase
from problems.N1444_Number_Of_Ways_Of_Cutting_A_Pizza import Solution

class TestSolution(TestCase):
    def test_ways(self):
        self.assertEqual(3, Solution().ways(pizza = ["A..","AAA","..."], k = 3))

    def test_ways_1(self):
        self.assertEqual(1, Solution().ways(pizza = ["A..","AA.","..."], k = 3))

    def test_ways_2(self):
        self.assertEqual(1, Solution().ways(pizza = ["A..","A..","..."], k = 1))