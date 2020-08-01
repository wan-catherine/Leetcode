from unittest import TestCase
from problems.N930_Binary_Subarrays_With_Sum import Solution

class TestSolution(TestCase):
    def test_numSubarraysWithSum(self):
        self.assertEqual(4, Solution().numSubarraysWithSum(A = [1,0,1,0,1], S = 2))

    def test_numSubarraysWithSum_1(self):
        self.assertEqual(15, Solution().numSubarraysWithSum(A = [0, 0, 0, 0, 0], S = 0))
