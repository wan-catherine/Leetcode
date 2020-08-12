from unittest import TestCase
from problems.SearchRotatedSortedArrayII import Solution

class TestSolution(TestCase):
    def test_search(self):
        solution = Solution()
        res = solution.search([2,5,6,0,0,1,2], 0)
        self.assertEqual(res, True)

    def test_search_false(self):
        solution = Solution()
        res = solution.search([2,5,6,0,0,1,2], 3)
        self.assertEqual(res, False)

    def test_search_1(self):
        solution = Solution()
        res = solution.search([1], 1)
        self.assertEqual(res, True)

    def test_search_2(self):
        solution = Solution()
        res = solution.search([3,1], 0)
        self.assertEqual(res, False)

    def test_search_3(self):
        solution = Solution()
        res = solution.search([1,3,5], 3)
        self.assertEqual(res, True)

    def test_search_4(self):
        solution = Solution()
        res = solution.search([1,1,3,1], 3)
        self.assertEqual(res, True)

    def test_search_5(self):
        solution = Solution()
        res = solution.search([1,3,1,1,1], 3)
        self.assertEqual(res, True)

    def test_search_6(self):
        solution = Solution()
        res = solution.search([3,1,1,1], 3)
        self.assertEqual(res, True)
