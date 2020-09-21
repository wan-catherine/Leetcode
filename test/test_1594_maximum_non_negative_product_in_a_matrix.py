from unittest import TestCase
from problems.N1594_Maximum_Non_Negative_Product_In_A_Matrix import Solution

class TestSolution(TestCase):
    def test_maxProductPath(self):
        grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
        self.assertEqual(-1, Solution().maxProductPath(grid))

    def test_maxProductPath_1(self):
        grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
        self.assertEqual(8, Solution().maxProductPath(grid))

    def test_maxProductPath_2(self):
        grid = [[1, 3],
               [0,-4]]
        self.assertEqual(0, Solution().maxProductPath(grid))

    def test_maxProductPath_3(self):
        grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
        self.assertEqual(2, Solution().maxProductPath(grid))
