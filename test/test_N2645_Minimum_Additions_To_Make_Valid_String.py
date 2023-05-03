from unittest import TestCase
from problems.N2645_Minimum_Additions_To_Make_Valid_String import Solution

class TestSolution(TestCase):
    def test_add_minimum(self):
        self.assertEqual(2, Solution().addMinimum("b"))

    def test_add_minimum_1(self):
        self.assertEqual(6, Solution().addMinimum("aaa"))

    def test_add_minimum_2(self):
        self.assertEqual(0, Solution().addMinimum("abc"))


