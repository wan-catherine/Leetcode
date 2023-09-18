from unittest import TestCase
from problems.N2751_Robot_Collisions import Solution

class TestSolution(TestCase):
    def test_survived_robots_healths(self):
        self.assertListEqual([2,17,9,15,10], Solution().survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"))

    def test_survived_robots_healths_1(self):
        self.assertListEqual([14], Solution().survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"))

    def test_survived_robots_healths_2(self):
        self.assertListEqual([], Solution().survivedRobotsHealths(positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"))

    def test_survived_robots_healths_3(self):
        self.assertListEqual([16], Solution().survivedRobotsHealths(positions = [13,3], healths = [17,2], directions = "LR"))
