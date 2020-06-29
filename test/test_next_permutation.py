from unittest import TestCase
from problems.NextPermutation import Solution

class TestSolution(TestCase):
    def test_nextPermutation(self):
        solution = Solution()
        res = solution.nextPermutation([1,2,3])
        self.assertEqual([1,3,2], res)

    def test_nextPermutation_1(self):
        solution = Solution()
        res = solution.nextPermutation([3,2,1])
        self.assertEqual([1,2,3], res)

    def test_nextPermutation_2(self):
        solution = Solution()
        res = solution.nextPermutation([6,2,1,5,4,3,0])
        self.assertEqual([6,2,3,0,1,4,5], res)

    def test_nextPermutation_3(self):
        solution = Solution()
        res = solution.nextPermutation([5,1,1])
        self.assertEqual([1,1,5], res)