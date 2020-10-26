from unittest import TestCase
from problems.N1632_Rank_Transform_Of_A_Matrix import Solution

class TestSolution(TestCase):
    def test_matrixRankTransform(self):
        self.assertListEqual([[1,2],[2,3]], Solution().matrixRankTransform([[1,2],[3,4]]))

    def test_matrixRankTransform_1(self):
        self.assertListEqual([[1,1],[1,1]], Solution().matrixRankTransform([[7,7],[7,7]]))

    def test_matrixRankTransform_2(self):
        self.assertListEqual([[4,2,3],[1,3,4],[5,1,6],[1,3,4]], Solution().matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))

    def test_matrixRankTransform_3(self):
        self.assertListEqual([[5,1,4],[1,2,3],[6,3,1]], Solution().matrixRankTransform([[7,3,6],[1,4,5],[9,8,2]]))

    def test_matrixRankTransform_4(self):
        self.assertListEqual([[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]], Solution().matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]))

    def test_matrixRankTransform_5(self):
        self.assertListEqual([[3,4,1,2,7],[9,5,3,10,8],[4,6,2,7,5],[7,9,8,1,6],[12,10,4,5,11]], Solution().matrixRankTransform([[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]))