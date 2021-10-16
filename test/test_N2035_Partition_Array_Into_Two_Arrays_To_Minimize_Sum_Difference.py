from unittest import TestCase
from problems.N2035_Partition_Array_Into_Two_Arrays_To_Minimize_Sum_Difference import Solution

class TestSolution(TestCase):
    def test_minimum_difference(self):
        self.assertEqual(2, Solution().minimumDifference([3,9,7,3]))

    def test_minimum_difference_1(self):
        self.assertEqual(72, Solution().minimumDifference([-36,36]))

    def test_minimum_difference_2(self):
        self.assertEqual(0, Solution().minimumDifference([2,-1,0,4,-2,-9]))