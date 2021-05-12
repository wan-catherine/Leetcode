from unittest import TestCase
from problems.N1269_Number_Of_Ways_To_Stay_In_The_Same_Place_After_Some_Steps import Solution

class TestSolution(TestCase):
    def test_num_ways(self):
        self.assertEqual(4, Solution().numWays(3, 2))

    def test_num_ways_1(self):
        self.assertEqual(2, Solution().numWays(2, 4))

    def test_num_ways_2(self):
        self.assertEqual(8, Solution().numWays(4, 2))
