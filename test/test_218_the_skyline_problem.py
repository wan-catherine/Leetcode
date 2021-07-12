from unittest import TestCase
from problems.N218_The_Skyline_Problem import Solution

class TestSolution(TestCase):
    def test_getSkyline(self):
        self.assertListEqual([ [2,10], [3,15], [7,12], [12,0], [15,10], [20,8], [24,0] ], Solution().getSkyline_segmenttree([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]))