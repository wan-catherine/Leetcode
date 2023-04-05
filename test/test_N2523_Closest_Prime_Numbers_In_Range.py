from unittest import TestCase
from problems.N2523_Closest_Prime_Numbers_In_Range import Solution

class TestSolution(TestCase):
    def test_closest_primes(self):
        self.assertListEqual([11,13], Solution().closestPrimes(left = 10, right = 19))

    def test_closest_primes_1(self):
        self.assertListEqual([-1,-1], Solution().closestPrimes(left = 4, right = 6))

    def test_closest_primes_2(self):
        self.assertListEqual([2,3], Solution().closestPrimes(left = 1, right = 1000000))



