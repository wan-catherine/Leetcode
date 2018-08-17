from unittest import TestCase
from problems.ThreeSum import Solution

class TestSolution(TestCase):
    def test_threeSum_with_list(self):
        solution = Solution()
        res = solution.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertEquals([[-1, -1, 2], [-1, 0, 1]], res)

    def test_threeSum_with_new_list(self):
        solution = Solution()
        res = solution.threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0])
        self.assertEquals([[-5,1,4],[-3,-1,4],[-3,0,3],[-2,-1,3],[-2,1,1],[-1,0,1],[0,0,0]], res)