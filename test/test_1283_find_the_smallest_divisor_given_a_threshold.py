from unittest import TestCase
from problems.N1283_Find_The_Smallest_Divisor_Given_A_Threshold import Solution

class TestSolution(TestCase):
    def test_smallestDivisor(self):
        self.assertEqual(5, Solution().smallestDivisor(nums = [1,2,5,9], threshold = 6))

    def test_smallestDivisor_1(self):
        self.assertEqual(3, Solution().smallestDivisor(nums = [2,3,5,7,11], threshold = 11))

    def test_smallestDivisor_2(self):
        self.assertEqual(4, Solution().smallestDivisor(nums = [19], threshold = 5))

    def test_smallestDivisor_3(self):
        self.assertEqual(1, Solution().smallestDivisor([1,2,3],1000000))
