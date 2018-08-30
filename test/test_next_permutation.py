from unittest import TestCase
from problems.NextPermutation import Solution

class TestSolution(TestCase):
    def test_nextPermutation(self):
        solution = Solution()
        res = solution.nextPermutation([1,2,3])
        self.assertEqual([1,3,2], res)
