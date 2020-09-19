from unittest import TestCase
from problems.N1589_Maximum_Sum_Obtained_Of_Any_Permutation import Solution

class TestSolution(TestCase):
    def test_maxSumRangeQuery(self):
        self.assertEqual(19, Solution().maxSumRangeQuery(nums = [1,2,3,4,5], requests = [[1,3],[0,1]]))

    def test_maxSumRangeQuery_1(self):
        self.assertEqual(11, Solution().maxSumRangeQuery(nums = [1,2,3,4,5,6], requests = [[0,1]]))

    def test_maxSumRangeQuery_2(self):
        self.assertEqual(47, Solution().maxSumRangeQuery(nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]))

