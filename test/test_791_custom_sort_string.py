from unittest import TestCase
from problems.N791_Custom_Sort_String import Solution

class TestSolution(TestCase):
    def test_customSortString(self):
        self.assertEqual("cbad", Solution().customSortString("cba", "abcd"))