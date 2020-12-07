from unittest import TestCase
from problems.SpiralMatrix import Solution

class TestSolution(TestCase):
    def test_spiralOrder(self):
        solution = Solution()
        input = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
        res = solution.spiralOrder(input)
        self.assertEqual([1,2,3,6,9,8,7,4,5], res)

    def test_spiralOrder_four(self):
        solution = Solution()
        input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
        res = solution.spiralOrder(input)
        self.assertEqual([1,2,3,4,8,12,11,10,9,5,6,7], res)

    def test_spiralOrder_more(self):
        solution = Solution()
        input = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        res = solution.spiralOrder(input)
        self.assertEqual([1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13], res)

    def test_spiralOrder_1(self):
        solution = Solution()
        input = [[3],[2]]
        res = solution.spiralOrder(input)
        self.assertEqual([3,2], res)

    def test_spiralOrder_2(self):
        solution = Solution()
        input = [[2,5],[8,4],[0,-1]]
        res = solution.spiralOrder(input)
        self.assertEqual([2, 5, 4, -1, 0, 8], res)