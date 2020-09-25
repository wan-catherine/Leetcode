from unittest import TestCase
from problems.N1227_Airplane_Seat_Assignment_Probability import Solution

class TestSolution(TestCase):
    def test_nthPersonGetsNthSeat(self):
        self.assertEqual(1.0, Solution().nthPersonGetsNthSeat(1))

    def test_nthPersonGetsNthSeat_1(self):
        self.assertEqual(0.5, Solution().nthPersonGetsNthSeat(2))
