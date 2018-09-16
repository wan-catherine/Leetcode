from unittest import TestCase
from problems.PermutationSequence import Solution

class TestSolution(TestCase):
    def test_getPermutation(self):
        solution = Solution()
        res = solution.getPermutation(3,3)
        self.assertEqual(res, "213")

    def test_getPermutation_4(self):
        solution = Solution()
        res = solution.getPermutation(4,9)
        self.assertEqual(res, "2314")

