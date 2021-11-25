from unittest import TestCase
from problems.N1588_Sum_Of_All_Odd_Length_Subarrays import Solution

class TestSolution(TestCase):
    def test_sum_odd_length_subarrays(self):
        self.assertEqual(58, Solution().sumOddLengthSubarrays([1,4,2,5,3]))
