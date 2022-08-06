from unittest import TestCase
from problems.N2366_Minimum_Replacements_To_Sort_The_Array import Solution

class TestSolution(TestCase):
    def test_minimum_replacement(self):
        self.assertEqual(2, Solution().minimumReplacement([3,9,3]))

    def test_minimum_replacement_1(self):
        self.assertEqual(0, Solution().minimumReplacement([1,2,3,4,5]))
