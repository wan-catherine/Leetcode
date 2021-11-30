from unittest import TestCase
from problems.N2088_Count_Fertile_Pyramids_In_A_Land import Solution

class TestSolution(TestCase):
    def test_count_pyramids(self):
        self.assertEqual(2, Solution().countPyramids([[0,1,1,0],[1,1,1,1]]))

    def test_count_pyramids_1(self):
        self.assertEqual(2, Solution().countPyramids([[1,1,1],[1,1,1]]))

    def test_count_pyramids_3(self):
        self.assertEqual(0, Solution().countPyramids([[1,0,1],[0,0,0],[1,0,1]]))

    def test_count_pyramids_4(self):
        self.assertEqual(13, Solution().countPyramids([[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]))


