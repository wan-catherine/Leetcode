from unittest import TestCase
from problems.N2762_Continuous_Subarrays import Solution

class TestSolution(TestCase):
    def test_continuous_subarrays(self):
        self.assertEquals(8, Solution().continuousSubarrays(nums = [5,4,2,4]))

    def test_continuous_subarrays_1(self):
        self.assertEquals(6, Solution().continuousSubarrays([1,2,3]))
