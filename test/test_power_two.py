from unittest import TestCase
from problems.PowerTwo import Solution

class TestSolution(TestCase):
    def test_isPowerOfTwo(self):
        solution = Solution()
        res = solution.isPowerOfTwo(1)
        self.assertEqual(True, res)

    def test_isPowerOfTwo_one(self):
        solution = Solution()
        res = solution.isPowerOfTwo(16)
        self.assertEqual(True, res)

    def test_isPowerOfTwo_two(self):
        solution = Solution()
        res = solution.isPowerOfTwo(218)
        self.assertEqual(False, res)