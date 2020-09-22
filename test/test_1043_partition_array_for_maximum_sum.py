from unittest import TestCase
from problems.N1043_Partition_Array_For_Maximum_Sum import Solution

class TestSolution(TestCase):
    def test_maxSumAfterPartitioning(self):
        self.assertEqual(84, Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))

    def test_maxSumAfterPartitioning_1(self):
        self.assertEqual(83, Solution().maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))

    def test_maxSumAfterPartitioning_2(self):
        self.assertEqual(1, Solution().maxSumAfterPartitioning(arr = [1], k = 1))