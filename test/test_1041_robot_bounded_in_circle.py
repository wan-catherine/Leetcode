from unittest import TestCase
from problems.N1041_Robot_Bounded_In_Circle import Solution

class TestSolution(TestCase):
    def test_isRobotBounded(self):
        self.assertTrue(Solution().isRobotBounded("GGLLGG"))

    def test_isRobotBounded_1(self):
        self.assertFalse(Solution().isRobotBounded("GG"))

    def test_isRobotBounded_2(self):
        self.assertTrue(Solution().isRobotBounded("GL"))
