from unittest import TestCase
from problems.N3362_Zero_Array_Transformation_III import Solution

class TestSolution(TestCase):
    def test_max_removal(self):
        self.assertEquals(1, Solution().maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]))

    def test_max_removal_1(self):
        self.assertEquals(2, Solution().maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]))

    def test_max_removal_2(self):
        self.assertEquals(-1, Solution().maxRemoval(nums = [1,2,3,4], queries = [[0,3]]))
