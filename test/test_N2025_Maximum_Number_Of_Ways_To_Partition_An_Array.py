from unittest import TestCase
from problems.N2025_Maximum_Number_Of_Ways_To_Partition_An_Array import Solution

class TestSolution(TestCase):
    def test_ways_to_partition(self):
        self.assertEqual(1, Solution().waysToPartition(nums = [2,-1,2], k = 3))

    def test_ways_to_partition_1(self):
        self.assertEqual(2, Solution().waysToPartition(nums = [0,0,0], k = 1))

    def test_ways_to_partition_2(self):
        self.assertEqual(4, Solution().waysToPartition(nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33))
