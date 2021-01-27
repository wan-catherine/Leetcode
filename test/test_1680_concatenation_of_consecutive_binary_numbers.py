from unittest import TestCase
from problems.N1680_Concatenation_Of_Consecutive_Binary_Numbers import Solution

class TestSolution(TestCase):
    def test_concatenatedBinary(self):
        self.assertEqual(1, Solution().concatenatedBinary(1))

    def test_concatenatedBinary_1(self):
        self.assertEqual(27, Solution().concatenatedBinary(3))

    def test_concatenatedBinary_2(self):
        self.assertEqual(505379714, Solution().concatenatedBinary(12))
