from unittest import TestCase
from problems.N481_Magical_String import Solution

class TestSolution(TestCase):
    def test_magical_string(self):
        self.assertEqual(3, Solution().magicalString(6))

    def test_magical_string_1(self):
        self.assertEqual(1, Solution().magicalString(1))
