from unittest import TestCase
from problems.MaximalSquare import Solution

class TestSolution(TestCase):
    def test_maximalSquare(self):
        solution = Solution()
        res = solution.maximalSquare([['1','0','1','0','0'],['1','0','1','1','1'],
                                      ['1','1','1','1','1'],['1','0','0','1','0']])
        self.assertEqual(4, res)


    def test_maximalSquare_one(self):
        solution = Solution()
        res = solution.maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]])
        self.assertEqual(4, res)

    def test_maximalSquare_1(self):
        solution = Solution()
        square = [["1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","0","0","1","1","1","1","1","1","1","1","0","0","1","1","1","0","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","0","1","1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","0","1","1","0","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0","1","1","0","0","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","0","1","1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","0","1","0","1","1","1","1","1","1","0","1","1","1","1"],["0","1","1","0","1","1","0","1","0","1","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0","1","0","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","0","0","1","1","0","0","1","1","0","1","1","0","1","0","1","0","1"],["1","1","1","1","0","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","1","1","0","1","0","1","1","0","1","0","1","1"],["1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1","1"],["1","1","1","0","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1","1","1","0","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","1","1","0","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0","1","1"],["1","1","1","1","1","0","0","1","1","1","1","1","1","1","1","0","1","0","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","0","1","1","1","1","1","1","0","0","1","1","1","1","1"],["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0","1","1","1"],["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","0","1","1","1","1","1","0","0","1","0","1","1","1","1","1","0","1","1","1","1","1","1"],["1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","0","1","1","1","1","1","0","1","1","1","1","1","0","1","1","0","1","1"],["1","1","0","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","0","1","0","1","1","1","0","0","1","1","1","1","1","1","1","1"],["1","1","1","0","0","1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","0","1","1","1","1","0","1","1","1","1","1","0","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0","1","1","1","1","1","1","0","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","1","1","0","0","1","1","1","1","1","1","1","1","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","0","0","1","1","1","1","1","1","1","1","1","0","1","1","1","0","1"],["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","0","1","1","1","0","1","1","0","1","1"],["1","1","1","1","0","1","1","0","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","0","0","0","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","1","1","1","0","1","0","1","0","1","1","0","1","1","1","1","1","1","1","1"],["1","0","1","1","0","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1"],["1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","1","1","1"],["0","1","1","1","1","0","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","0","1","1","1","1","0","1","1","1","1","1","1","0","1","0","1","1","0","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","1","1","1","0"],["1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0","0","1","1","1","1"],["1","1","0","1","1","0","1","1","1","1","1","1","0","1","0","1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","0","1","1","1","0","1","0","1","0","0"],["0","1","1","0","1","1","1","1","1","1","1","0","0","1","1","1","1","1","0","0","1","0","1","1","1","1","1","0","1","1","1","0","1","1","0","1","1","1","0","1"]]
        res = solution.maximalSquare(square)
        self.assertEqual(64, res)
