from unittest import TestCase
from problems.N351_Android_Unlock_Patterns import Solution

class TestSolution(TestCase):
    def test_number_of_patterns(self):
        self.assertEqual(9, Solution().numberOfPatterns(1, 1))

    def test_number_of_patterns_1(self):
        self.assertEqual(65, Solution().numberOfPatterns(1, 2))
