from unittest import TestCase
from problems.SearchInsertPosition import Solution

class TestSolution(TestCase):
    def test_searchInsert(self):
        solution = Solution()
        res = solution.searchInsert([1,3,5,6], 5)
        self.assertEqual(2, res)

    def test_searchInsert_zero(self):
        solution = Solution()
        res = solution.searchInsert([1,3,5,6], 0)
        self.assertEqual(0, res)

