from unittest import TestCase
from problems.N786_Kth_Smallest_Prime_Fraction import Solution

class TestSolution(TestCase):
    def test_kthSmallestPrimeFraction(self):
        self.assertListEqual([2, 5], Solution().kthSmallestPrimeFraction(A = [1, 2, 3, 5], K = 3))

    def test_kthSmallestPrimeFraction_1(self):
        self.assertListEqual([1, 7], Solution().kthSmallestPrimeFraction(A = [1, 7], K = 1))
