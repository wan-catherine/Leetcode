from unittest import TestCase
from problems.N2518_Number_Of_Great_Partitions import Solution

class TestSolution(TestCase):
    def test_count_partitions(self):
        self.assertEqual(6, Solution().countPartitions(nums = [1,2,3,4], k = 4))

    def test_count_partitions_1(self):
        self.assertEqual(0, Solution().countPartitions(nums = [3,3,3], k = 4))

    def test_count_partitions_2(self):
        self.assertEqual(2, Solution().countPartitions(nums = [6,6], k = 2))
