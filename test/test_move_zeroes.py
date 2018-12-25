from unittest import TestCase
from problems.MoveZeroes import Solution

class TestSolution(TestCase):
    def test_moveZeroes(self):
        solution = Solution()
        l = [0,1,0,3,12]
        solution.moveZeroes(l)
        self.assertEqual(l, [1,3,12,0,0])
