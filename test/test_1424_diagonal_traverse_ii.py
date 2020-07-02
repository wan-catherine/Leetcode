from unittest import TestCase
from problems.N1424_Diagonal_Traverse_II import Solution

class TestSolution(TestCase):
    def test_findDiagonalOrder(self):
        nums = [[1,2,3],[4,5,6],[7,8,9]]
        output = [1,4,2,7,5,3,8,6,9]
        self.assertListEqual(output, Solution().findDiagonalOrder(nums))

    def test_findDiagonalOrder_1(self):
        nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
        output = [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
        self.assertListEqual(output, Solution().findDiagonalOrder(nums))

    def test_findDiagonalOrder_2(self):
        nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
        output = [1,4,2,5,3,8,6,9,7,10,11]
        self.assertListEqual(output, Solution().findDiagonalOrder(nums))

    def test_findDiagonalOrder_3(self):
        nums = [[1,2,3,4,5,6]]
        output = [1,2,3,4,5,6]
        self.assertListEqual(output, Solution().findDiagonalOrder(nums))
