from unittest import TestCase
from problems.N1488_Avoid_Flood_In_The_City import Solution

class TestSolution(TestCase):
    def test_avoidFlood(self):
        rains = [1, 2, 3, 4]
        self.assertListEqual([-1,-1,-1,-1], Solution().avoidFlood(rains))

    def test_avoidFlood_1(self):
        rains = [1,2,0,0,2,1]
        self.assertListEqual([-1,-1,2,1,-1,-1], Solution().avoidFlood(rains))

    def test_avoidFlood_2(self):
        rains = [1,2,0,1,2]
        self.assertListEqual([], Solution().avoidFlood(rains))

    def test_avoidFlood_3(self):
        rains = [69,0,0,0,69]
        self.assertListEqual([-1,69,1,1,-1], Solution().avoidFlood(rains))

    def test_avoidFlood_4(self):
        rains = [10,20,20]
        self.assertListEqual([], Solution().avoidFlood(rains))

    def test_avoidFlood_5(self):
        rains = [0,1,1]
        self.assertListEqual([], Solution().avoidFlood(rains))

    def test_avoidFlood_6(self):
        rains = [1,0,2,3,0,1,2]
        self.assertListEqual([-1,1,-1,-1,2,-1,-1], Solution().avoidFlood(rains))
