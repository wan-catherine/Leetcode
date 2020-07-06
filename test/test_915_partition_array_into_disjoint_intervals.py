from unittest import TestCase
from problems.N915_Partition_Array_Into_Disjoint_Intervals import Solution

class TestSolution(TestCase):
    def test_partitionDisjoint(self):
        self.assertEqual(3, Solution().partitionDisjoint([5,0,3,8,6]))

    def test_partitionDisjoint_1(self):
        self.assertEqual(4, Solution().partitionDisjoint([1,1,1,0,6,12]))