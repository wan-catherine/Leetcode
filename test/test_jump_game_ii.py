from unittest import TestCase
from problems.JumpGameII import Solution

class TestSolution(TestCase):
    def test_jump(self):
        solution = Solution()
        res = solution.jump([2,3,1,1,4])
        self.assertEqual(2, res)

    def test_jump_zero(self):
        solution = Solution()
        res = solution.jump([0])
        self.assertEqual(0, res)
