from unittest import TestCase
from problems.N2411_Smallest_Subarrays_With_Maximum_Bitwise_OR import Solution

class TestSolution(TestCase):
    def test_smallest_subarrays(self):
        self.assertListEqual([3,3,2,2,1], Solution().smallestSubarrays([1,0,2,1,3]))

    def test_smallest_subarrays_1(self):
        self.assertListEqual([2,1], Solution().smallestSubarrays([1,2]))