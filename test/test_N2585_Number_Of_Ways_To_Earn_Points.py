from unittest import TestCase
from problems.N2585_Number_Of_Ways_To_Earn_Points import Solution

class TestSolution(TestCase):
    def test_ways_to_reach_target(self):
        self.assertEqual(7, Solution().waysToReachTarget(target = 6, types = [[6,1],[3,2],[2,3]]))

    def test_ways_to_reach_target_1(self):
        self.assertEqual(4, Solution().waysToReachTarget(target = 5, types = [[50,1],[50,2],[50,5]]))

    def test_ways_to_reach_target_2(self):
        self.assertEqual(1, Solution().waysToReachTarget(target = 18, types = [[6,1],[3,2],[2,3]]))
