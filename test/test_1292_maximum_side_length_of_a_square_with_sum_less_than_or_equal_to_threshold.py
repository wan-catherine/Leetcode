from unittest import TestCase
from problems.N1292_Maximum_Side_Length_Of_A_Square_With_Sum_Less_Than_Or_Equal_To_Threshold import Solution

class TestSolution(TestCase):
    def test_maxSideLength(self):
        self.assertEqual(2, Solution().maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))

    def test_maxSideLength_1(self):
        self.assertEqual(0, Solution().maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1))

    def test_maxSideLength_2(self):
        self.assertEqual(3, Solution().maxSideLength(mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6))

    def test_maxSideLength_2(self):
        self.assertEqual(2, Solution().maxSideLength(mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184))