from unittest import TestCase
from problems.ReverseBits import Solution

class TestSolution(TestCase):
    def test_reverseBits(self):
        solution = Solution()
        res = solution.reverseBits(43261596)
        self.assertEqual(964176192, res)
