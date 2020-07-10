from unittest import TestCase
from problems.N1031_Maximum_Sum_Of_Two_Non_Overlapping_Subarrays import Solution

class TestSolution(TestCase):
    def test_maxSumTwoNoOverlap(self):
        self.assertEqual(20, Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))

    def test_maxSumTwoNoOverlap_1(self):
        self.assertEqual(29, Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2))

    def test_maxSumTwoNoOverlap_2(self):
        self.assertEqual(31, Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3))
