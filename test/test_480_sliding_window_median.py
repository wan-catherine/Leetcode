from unittest import TestCase
from problems.N480_Sliding_Window_Median import Solution

class TestSolution(TestCase):
    def test_medianSlidingWindow(self):
        self.assertListEqual([1,-1,-1,3,5,6], Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
