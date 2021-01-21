from unittest import TestCase
from problems.N1728_Cat_And_Mouse_II import Solution

class TestSolution(TestCase):
    def test_canMouseWin(self):
        self.assertTrue(Solution().canMouseWin(grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2))

    def test_canMouseWin_1(self):
        self.assertTrue(Solution().canMouseWin(grid = ["M.C...F"], catJump = 1, mouseJump = 4))

    def test_canMouseWin_2(self):
        self.assertFalse(Solution().canMouseWin(grid = ["M.C...F"], catJump = 1, mouseJump = 3))

    def test_canMouseWin_3(self):
        self.assertFalse(Solution().canMouseWin(grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5))

    def test_canMouseWin_4(self):
        self.assertTrue(Solution().canMouseWin(grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1))
