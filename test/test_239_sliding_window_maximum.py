from unittest import TestCase
from problems.N239_Sliding_Window_Maximum import Solution

class TestSolution(TestCase):
    def test_maxSlidingWindow(self):
        self.assertListEqual([3,3,5,5,6,7], Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

    def test_maxSlidingWindow_1(self):
        self.assertListEqual([3,3,2,5], Solution().maxSlidingWindow([1,3,1,2,0,5],3))

    def test_maxSlidingWindow_2(self):
        self.assertListEqual([1,-1], Solution().maxSlidingWindow([1,-1],1))

    def test_maxSlidingWindow_3(self):
        self.assertListEqual([1], Solution().maxSlidingWindow([1],1))

    def test_maxSlidingWindow_4(self):
        self.assertListEqual([11], Solution().maxSlidingWindow([9,11],2))
