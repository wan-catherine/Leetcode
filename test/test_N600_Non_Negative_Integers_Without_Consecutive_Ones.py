from unittest import TestCase
from problems.N600_Non_Negative_Integers_Without_Consecutive_Ones import Solution

class TestSolution(TestCase):
    def test_find_integers(self):
        self.assertEqual(5, Solution().findIntegers(5))

    def test_find_integers_1(self):
        self.assertEqual(3, Solution().findIntegers(3))

    def test_find_integers_2(self):
        self.assertEqual(5, Solution().findIntegers(6))
