from unittest import TestCase
from problems.N5436_Running_Sum_Of_1d_Array import Solution

class TestSolution(TestCase):
    def test_runningSum(self):
        self.assertListEqual([1,3,6,10], Solution().runningSum([1,2,3,4]))

    def test_runningSum_1(self):
        self.assertListEqual([1,2,3,4,5], Solution().runningSum([1,1,1,1,1]))

    def test_runningSum_2(self):
        self.assertListEqual([3,4,6,16,17], Solution().runningSum([3,1,2,10,1]))
