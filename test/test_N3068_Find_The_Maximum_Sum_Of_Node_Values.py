from unittest import TestCase
from problems.N3068_Find_The_Maximum_Sum_Of_Node_Values import Solution

class TestSolution(TestCase):
    def test_maximum_value_sum(self):
        self.assertEqual(6, Solution().maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]))

    def test_maximum_value_sum_1(self):
        self.assertEqual(9, Solution().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]))

    def test_maximum_value_sum_2(self):
        self.assertEqual(42, Solution().maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]))
