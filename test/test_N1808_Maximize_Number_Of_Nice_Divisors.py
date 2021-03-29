from unittest import TestCase
from problems.N1808_Maximize_Number_Of_Nice_Divisors import Solution

class TestSolution(TestCase):
    def test_max_nice_divisors(self):
        self.assertEqual(6, Solution().maxNiceDivisors(5))

    def test_max_nice_divisors_1(self):
        self.assertEqual(18, Solution().maxNiceDivisors(8))
