from unittest import TestCase
from problems.N1411_Number_Of_Ways_To_Paint_N3_Grid import Solution

class TestSolution(TestCase):
    def test_num_of_ways(self):
        self.assertEqual(12, Solution().numOfWays(1))

    def test_num_of_ways_1(self):
        self.assertEqual(54, Solution().numOfWays(2))

    def test_num_of_ways_2(self):
        self.assertEqual(246, Solution().numOfWays(3))

    def test_num_of_ways_3(self):
        self.assertEqual(106494, Solution().numOfWays(7))

    def test_num_of_ways_4(self):
        self.assertEqual(30228214, Solution().numOfWays(500))
