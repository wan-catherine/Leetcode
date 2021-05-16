from unittest import TestCase
from problems.N65_Valid_Number import Solution

class TestSolution(TestCase):
    def test_is_number(self):
        self.assertTrue(Solution().isNumber("0"))

    def test_is_number_1(self):
        self.assertFalse(Solution().isNumber("e"))

    def test_is_number_2(self):
        self.assertFalse(Solution().isNumber("."))

    def test_is_number_3(self):
        self.assertTrue(Solution().isNumber(".1"))
