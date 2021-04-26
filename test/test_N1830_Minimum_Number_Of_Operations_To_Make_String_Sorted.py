from unittest import TestCase
from problems.N1830_Minimum_Number_Of_Operations_To_Make_String_Sorted import Solution

class TestSolution(TestCase):
    def test_make_string_sorted(self):
        self.assertEqual(5, Solution().makeStringSorted("cba"))

    def test_make_string_sorted_1(self):
        self.assertEqual(2, Solution().makeStringSorted("aabaa"))

    def test_make_string_sorted_2(self):
        self.assertEqual(63, Solution().makeStringSorted("cdbea"))

    def test_make_string_sorted_3(self):
        self.assertEqual(982157772, Solution().makeStringSorted("leetcodeleetcodeleetcode"))
