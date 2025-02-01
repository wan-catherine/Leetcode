from unittest import TestCase
from problems.N827_Making_A_Large_Island import Solution

class TestSolution(TestCase):
    def test_largest_island(self):
        self.assertEquals(3, Solution().largestIsland([[1,0],[0,1]]))

    def test_largest_island_1(self):
        self.assertEquals(4, Solution().largestIsland([[1,1],[1,0]]))

    def test_largest_island_2(self):
        self.assertEquals(4, Solution().largestIsland([[1,1],[1,1]]))

    def test_largest_island_3(self):
        self.assertEquals(1, Solution().largestIsland([[0,0],[0,0]]))
