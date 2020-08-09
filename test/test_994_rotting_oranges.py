from unittest import TestCase
from problems.N994_Rotting_Oranges import Solution

class TestSolution(TestCase):
    def test_orangesRotting(self):
        self.assertEqual(4, Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

    def test_orangesRotting_1(self):
        self.assertEqual(-1, Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

    def test_orangesRotting_2(self):
        self.assertEqual(0, Solution().orangesRotting([[0,2]]))

    def test_orangesRotting_3(self):
        self.assertEqual(1, Solution().orangesRotting([[1,2]]))
