from unittest import TestCase
from problems.MaximumLengthPairChain import Solution

class TestSolution(TestCase):
    def test_find_longest_Chain_with_empty_pair(self):
        solution = Solution()
        res = solution.findLongestChain([])
        self.assertEquals(0, res)

    def test_find_longest_Chain_with_three_pairs(self):
        solution = Solution()
        res = solution.findLongestChain([[1,2], [2,3], [3,4]])
        self.assertEquals(2, res)

    def test_find_longest_Chain_with_four_pairs(self):
        solution = Solution()
        res = solution.findLongestChain([[1,2], [4,5], [3,6], [7,8]])
        self.assertEquals(3, res)
