from unittest import TestCase
from problems.N939_Minimum_Area_Rectangle import Solution

class TestSolution(TestCase):
    def test_minAreaRect(self):
        self.assertEqual(4, Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))

    def test_minAreaRect_1(self):
        self.assertEqual(2, Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

    def test_minAreaRect_2(self):
        self.assertEqual(0, Solution().minAreaRect([[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]))
