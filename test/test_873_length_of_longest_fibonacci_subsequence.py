from unittest import TestCase
from problems.N873_Length_Of_Longest_Fibonacci_Subsequence import Solution

class TestSolution(TestCase):
    def test_lenLongestFibSubseq(self):
        self.assertEqual(5, Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))

    def test_lenLongestFibSubseq_1(self):
        self.assertEqual(3, Solution().lenLongestFibSubseq([1,3,7,11,12,14,18]))
