from unittest import TestCase
from problems.N1503_Last_Moment_Before_All_Ants_Fall_Out_Of_A_Plank import Solution

class TestSolution(TestCase):
    def test_getLastMoment(self):
        n = 4
        left = [4, 3]
        right = [0, 1]
        self.assertEqual(4, Solution().getLastMoment(n, left, right))

    def test_getLastMoment_1(self):
        n = 7
        left = []
        right = [0,1,2,3,4,5,6,7]
        self.assertEqual(7, Solution().getLastMoment(n, left, right))

    def test_getLastMoment_2(self):
        n = 9
        left = [5]
        right = [4]
        self.assertEqual(5, Solution().getLastMoment(n, left, right))

    def test_getLastMoment_3(self):
        n = 7
        left = [0,1,2,3,4,5,6,7]
        right = []
        self.assertEqual(7, Solution().getLastMoment(n, left, right))

    def test_getLastMoment_4(self):
        n = 6
        left = [6]
        right = [0]
        self.assertEqual(6, Solution().getLastMoment(n, left, right))

