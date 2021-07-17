from unittest import TestCase
from problems.N1906_Minimum_Absolute_Difference_Queries import Solution

class TestSolution(TestCase):
    def test_min_difference(self):
        self.assertListEqual([2,1,4,1], Solution().minDifference(nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]))

    def test_min_difference_1(self):
        self.assertListEqual([-1,1,1,3], Solution().minDifference(nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]))

    def test_min_difference_2(self):
        self.assertListEqual([5,1,5,1,13,1,1,2,2,1], Solution().minDifference([4,2,15,1,14,6,2,9,4,5], [[7,8],[8,9],[7,8],[7,9],[3,4],[1,8],[5,9],[6,8],[0,2],[0,7]]))
