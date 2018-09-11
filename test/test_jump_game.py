from unittest import TestCase
from problems.JumpGame import Solution

class TestSolution(TestCase):
    def test_canJump(self):
        solution = Solution()
        res = solution.canJump([2,3,1,1,4])
        self.assertTrue(res)

    def test_canJump_false(self):
        solution = Solution()
        res = solution.canJump([3,2,1,0,4])
        self.assertFalse(res)

    def test_canJump_zero(self):
        solution = Solution()
        res = solution.canJump([0])
        self.assertTrue(res)
