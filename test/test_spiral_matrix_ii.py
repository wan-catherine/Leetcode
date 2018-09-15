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