from unittest import TestCase
from problems.N1888_Minimum_Number_Of_Flips_To_Make_The_Binary_String_Alternating import Solution

class TestSolution(TestCase):
    def test_min_flips(self):
        self.assertEqual(2, Solution().minFlips("111000"))

    def test_min_flips_1(self):
        self.assertEqual(0, Solution().minFlips("010"))

    def test_min_flips_2(self):
        self.assertEqual(1, Solution().minFlips("1110"))

    def test_min_flips_3(self):
        self.assertEqual(5, Solution().minFlips("10001100101000000"))