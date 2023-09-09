from unittest import TestCase
from problems.N2787_Ways_To_Express_An_Integer_As_Sum_Of_Powers import Solution

class TestSolution(TestCase):
    def test_number_of_ways(self):
        self.assertEquals(1, Solution().numberOfWays(n = 10, x = 2))

    def test_number_of_ways_1(self):
        self.assertEquals(2, Solution().numberOfWays(n = 4, x = 1))
