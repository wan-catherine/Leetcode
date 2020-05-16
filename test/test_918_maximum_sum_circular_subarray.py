from unittest import TestCase
from problems.N918_Maximum_Sum_Circular_Subarrary import Solution

class TestSolution(TestCase):
    def test_maxSubarraySumCircular(self):
        self.assertEqual(3, Solution().maxSubarraySumCircular([1,-2,3,-2]))

    def test_maxSubarraySumCircular_1(self):
        self.assertEqual(10, Solution().maxSubarraySumCircular([5,-3,5]))

    def test_maxSubarraySumCircular_2(self):
        self.assertEqual(4, Solution().maxSubarraySumCircular([3,-1,2,-1]))

    def test_maxSubarraySumCircular_3(self):
        self.assertEqual(3, Solution().maxSubarraySumCircular([3,-2,2,-3]))

    def test_maxSubarraySumCircular_4(self):
        self.assertEqual(-1, Solution().maxSubarraySumCircular([-2,-3,-1]))

