from unittest import TestCase
from problems.SpiralMatrixII import Solution

class TestSolution(TestCase):
    def test_generateMatrix(self):
        solution = Solution()
        res = solution.generateMatrix(3)
        expected = [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
        self.assertEqual(res, expected)

    def test_generateMatrix_1(self):
        solution = Solution()
        res = solution.generateMatrix(4)
        expected = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
        self.assertEqual(res, expected)