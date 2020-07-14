from unittest import TestCase
from problems.N1344_Angle_Between_Hands_Of_A_Clock import Solution

class TestSolution(TestCase):
    def test_angleClock(self):
        self.assertEqual(165, Solution().angleClock(12,30))

    def test_angleClock_1(self):
        self.assertEqual(75, Solution().angleClock(3,30))

    def test_angleClock_2(self):
        self.assertEqual(7.5, Solution().angleClock(3,15))

    def test_angleClock_3(self):
        self.assertEqual(155, Solution().angleClock(4,50))

    def test_angleClock_4(self):
        self.assertEqual(0, Solution().angleClock(12,0))

    def test_angleClock_5(self):
        self.assertEqual(7.5, Solution().angleClock(3, 15))

