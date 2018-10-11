from unittest import TestCase
from problems.GrayCode import Solution

class TestSolution(TestCase):
    def test_grayCode(self):
        solution = Solution()
        res = solution.grayCode(0)
        self.assertEqual([0], res)

    def test_grayCode_two(self):
        solution = Solution()
        res = solution.grayCode(2)
        self.assertEqual([0,1,3,2], res)

    def test_grayCode_three(self):
        solution = Solution()
        res = solution.grayCode(3)
        self.assertEqual([0,1,3,2,6,7,5,4], res)
