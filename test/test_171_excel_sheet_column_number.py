from unittest import TestCase
from problems.N171_Excel_Sheet_Column_Number import Solution

class TestSolution(TestCase):
    def test_titleToNumber(self):
        self.assertEqual(1, Solution().titleToNumber('A'))

    def test_titleToNumber_1(self):
        self.assertEqual(28, Solution().titleToNumber('AB'))

    def test_titleToNumber_2(self):
        self.assertEqual(701, Solution().titleToNumber('ZY'))

