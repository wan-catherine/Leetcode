from unittest import TestCase
from problems.CountPrimes import Solution

class TestSolution(TestCase):
    def test_countPrimes(self):
        solution = Solution()
        res = solution.countPrimes(10)
        self.assertEqual(4, res)

    def test_countPrimes_one(self):
        solution = Solution()
        res = solution.countPrimes(3)
        self.assertEqual(1, res)

    def test_countPrimes_two(self):
        solution = Solution()
        res = solution.countPrimes(2)
        self.assertEqual(0, res)
