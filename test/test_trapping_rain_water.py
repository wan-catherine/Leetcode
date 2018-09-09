from unittest import TestCase
from problems.TrappingRainWater import Solution

class TestSolution(TestCase):
    def test_trap(self):
        solution = Solution()
        res = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        self.assertEqual(6, res)

    def test_trap_big(self):
        solution = Solution()
        res = solution.trap([5,2,1,2,1,5])
        self.assertEqual(14, res)

    def test_trap_empty(self):
        solution = Solution()
        res = solution.trap([])
        self.assertEqual(0, res)