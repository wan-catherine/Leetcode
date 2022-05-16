from unittest import TestCase
from problems.N2270_Number_Of_Ways_To_Split_Array import Solution

class TestSolution(TestCase):
    def test_ways_to_split_array(self):
        self.assertEqual(2, Solution().waysToSplitArray([10,4,-8,7]))

    def test_ways_to_split_array_1(self):
        self.assertEqual(2, Solution().waysToSplitArray([2,3,1,0]))
