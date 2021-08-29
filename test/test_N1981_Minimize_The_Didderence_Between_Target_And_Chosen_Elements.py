from unittest import TestCase
from problems.N1981_Minimize_The_Didderence_Between_Target_And_Chosen_Elements import Solution

class TestSolution(TestCase):
    def test_minimize_the_difference(self):
        self.assertEqual(0, Solution().minimizeTheDifference(mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13))

    def test_minimize_the_difference_1(self):
        self.assertEqual(94, Solution().minimizeTheDifference(mat = [[1],[2],[3]], target = 100))
