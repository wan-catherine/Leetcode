from unittest import TestCase
from problems.N2513_Minimize_The_Maximum_Of_Two_Arrays import Solution

class TestSolution(TestCase):
    def test_minimize_set(self):
        self.assertEqual(4, Solution().minimizeSet(divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3))

    def test_minimize_set_1(self):
        self.assertEqual(3, Solution().minimizeSet(divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1))

    def test_minimize_set_2(self):
        self.assertEqual(15, Solution().minimizeSet(divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2))
