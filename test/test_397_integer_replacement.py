from unittest import TestCase
from problems.N397_Integer_Replacement import Solution

class TestSolution(TestCase):
    def test_integerReplacement(self):
        self.assertEqual(3, Solution().integerReplacement(8))

    def test_integerReplacement_1(self):
        self.assertEqual(4, Solution().integerReplacement(7))

    def test_integerReplacement_2(self):
        self.assertEqual(4, Solution().integerReplacement(9))

    def test_integerReplacement_3(self):
        self.assertEqual(2, Solution().integerReplacement(3))
