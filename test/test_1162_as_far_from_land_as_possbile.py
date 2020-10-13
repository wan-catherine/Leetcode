from unittest import TestCase
from problems.N1162_As_Far_From_Land_As_Possible import Solution

class TestSolution(TestCase):
    def test_maxDistance(self):
        self.assertEqual(2, Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))

    def test_maxDistance_1(self):
        self.assertEqual(4, Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
