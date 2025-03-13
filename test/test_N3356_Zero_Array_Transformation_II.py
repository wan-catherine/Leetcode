from unittest import TestCase
from problems.N3356_Zero_Array_Transformation_II import Solution

class TestSolution(TestCase):
    def test_min_zero_array(self):
        self.assertEquals(2, Solution().minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))

    def test_min_zero_array_1(self):
        self.assertEquals(-1, Solution().minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))

    def test_min_zero_array_2(self):
        self.assertEquals(3, Solution().minZeroArray(nums = [10], queries = [[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]]))