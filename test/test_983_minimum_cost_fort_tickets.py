from unittest import TestCase
from problems.N983_Minimum_Cost_For_Tickets import Solution

class TestSolution(TestCase):
    def test_mincostTickets(self):
        self.assertEqual(11, Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))

    def test_mincostTickets_1(self):
        self.assertEqual(17, Solution().mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))

    def test_mincostTickets_2(self):
        self.assertEqual(6, Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [7,2,15]))