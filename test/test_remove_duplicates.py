from unittest import TestCase
from problems.RemoveDuplicatesSortedArray import Solution

class TestSolution(TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        res = solution.removeDuplicates([1,1,2])
        self.assertEqual(res, 2)

    def test_removeDuplicates_three(self):
        solution = Solution()
        res = solution.removeDuplicates([1,1,1,2,2,3,5,5,5,5])
        self.assertEqual(res, 4)
