from unittest import TestCase
from problems.N1016_Binary_String_With_Substrings_Representing_1_To_N import Solution

class TestSolution(TestCase):
    def test_queryString(self):
        self.assertTrue(Solution().queryString("0110", 3))

    def test_queryString_1(self):
        self.assertFalse(Solution().queryString("0110", 4))

    def test_queryString_2(self):
        self.assertTrue(Solution().queryString("1111000101", 5))

    def test_queryString_3(self):
        self.assertTrue(Solution().queryString("1", 1))
