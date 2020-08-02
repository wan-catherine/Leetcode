from unittest import TestCase
from problems.N1536_Minimum_Swaps_To_Arrange_A_Binary_Grid import Solution

class TestSolution(TestCase):
    def test_minSwaps(self):
        grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
        self.assertEqual(3, Solution().minSwaps(grid))

    def test_minSwaps_1(self):
        grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
        self.assertEqual(-1, Solution().minSwaps(grid))

    def test_minSwaps_2(self):
        grid = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
        self.assertEqual(0, Solution().minSwaps(grid))

    def test_minSwaps_3(self):
        grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
        self.assertEqual(2, Solution().minSwaps(grid))

    def test_minSwaps_4(self):
        grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
        self.assertEqual(2, Solution().minSwaps(grid))

    def test_minSwaps_5(self):
        grid = [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]
        self.assertEqual(4, Solution().minSwaps(grid))
