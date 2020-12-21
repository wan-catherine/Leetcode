from unittest import TestCase
from problems.N1697_Checking_Existence_Of_Edge_Length_Limited_Paths import Solution

class TestSolution(TestCase):
    def test_distanceLimitedPathsExist(self):
        self.assertListEqual([False,True], Solution().distanceLimitedPathsExist(n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]))

    def test_distanceLimitedPathsExist_1(self):
        self.assertListEqual([True, False], Solution().distanceLimitedPathsExist(n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]))