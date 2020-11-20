from unittest import TestCase
from problems.SearchRotatedSortedArray import Solution

class TestSolution(TestCase):
    def test_search(self):
        solution = Solution()
        res = solution.search([4,5,6,7,0,1,2], 0)
        self.assertEqual(4, res)

    def test_search_no(self):
        solution = Solution()
        res = solution.search([4,5,6,7,0,1,2], 3)
        self.assertEqual(-1, res)

    def test_search_one(self):
        solution = Solution()
        res = solution.search([2], 2)
        self.assertEqual(0, res)

    def test_search_two(self):
        solution = Solution()
        res = solution.search([1,2], 2)
        self.assertEqual(1, res)

    def test_search_three(self):
        solution = Solution()
        res = solution.search([2, 1], 1)
        self.assertEqual(1, res)

    def test_search_1(self):
        solution = Solution()
        res = solution.search([5,1,3], 3)
        self.assertEqual(2, res)