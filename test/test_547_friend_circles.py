from unittest import TestCase
from problems.N547_Friend_Circles import Solution

class TestSolution(TestCase):
    def test_findCircleNum(self):
        input = [[1,1,0],
 [1,1,0],
 [0,0,1]]
        self.assertEqual(2, Solution().findCircleNum(input))

    def test_findCircleNum_1(self):
        input = [[1,1,0],
 [1,1,1],
 [0,1,1]]
        self.assertEqual(1, Solution().findCircleNum(input))

    def test_findCircleNum_2(self):
        input = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
        self.assertEqual(1, Solution().findCircleNum(input))
