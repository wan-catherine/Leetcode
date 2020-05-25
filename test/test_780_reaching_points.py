from unittest import TestCase
from problems.N780_Reaching_Points import Solution

class TestSolution(TestCase):
    def test_reachingPoints(self):
        self.assertTrue(Solution().reachingPoints(1,1,3,5))

    def test_reachingPoints_1(self):
        self.assertFalse(Solution().reachingPoints(1,1,2,2))

    def test_reachingPoints_2(self):
        self.assertTrue(Solution().reachingPoints(1,1,1,1))

    def test_reachingPoints_3(self):
        self.assertFalse(Solution().reachingPoints(1,8,4,15))

    def test_reachingPoints_4(self):
        self.assertFalse(Solution().reachingPoints(10,4,10,20))

