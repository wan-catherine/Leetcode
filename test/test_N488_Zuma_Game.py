from unittest import TestCase
from problems.N488_Zuma_Game import Solution

class TestSolution(TestCase):
    def test_find_min_step(self):
        self.assertEqual(-1, Solution().findMinStep(board = "WRRBBW", hand = "RB"))

    def test_find_min_step_1(self):
        self.assertEqual(2, Solution().findMinStep(board = "WWRRBBWW", hand = "WRBRW"))

    def test_find_min_step_2(self):
        self.assertEqual(2, Solution().findMinStep(board = "G", hand = "GGGGG"))

    def test_find_min_step_3(self):
        self.assertEqual(2, Solution().findMinStep("RRWWRRBBRR", "WB"))

    def test_find_min_step_4(self):
        self.assertEqual(2, Solution().findMinStep("RRWWRRW", "WWRRR"))

    def test_find_min_step_5(self):
        self.assertEqual(-1, Solution().findMinStep("RRWWRRW", "WR"))

