from unittest import TestCase
from problems.N907_Sum_Of_Subarray_Minimus import Solution

class TestSolution(TestCase):
    def test_sumSubarrayMins(self):
        self.assertEqual(17, Solution().sumSubarrayMins([3,1,2,4]))

    def test_sumSubarrayMins_1(self):
        self.assertEqual(593, Solution().sumSubarrayMins([71,55,82,55]))
