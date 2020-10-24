from unittest import TestCase
from problems.N1362_Closest_Divisors import Solution

class TestSolution(TestCase):
    def test_closestDivisors(self):
        self.assertListEqual([3,3], Solution().closestDivisors(8))

    def test_closestDivisors_1(self):
        self.assertListEqual([5,25], Solution().closestDivisors(123))

    def test_closestDivisors_2(self):
        self.assertListEqual([40,25], Solution().closestDivisors(999))

    def test_closestDivisors_3(self):
        self.assertListEqual([1,2], Solution().closestDivisors(1))
