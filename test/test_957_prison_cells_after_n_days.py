from unittest import TestCase
from problems.N957_Prison_Cells_After_N_Days import Solution

class TestSolution(TestCase):
    def test_prisonAfterNDays(self):
        cells = [0, 1, 0, 1, 1, 0, 0, 1]
        N = 7
        output = [0,0,1,1,0,0,0,0]
        self.assertListEqual(output, Solution().prisonAfterNDays(cells, N))

    def test_prisonAfterNDays_1(self):
        cells = [1, 0, 0, 1, 0, 0, 1, 0]
        N = 1000000000
        output = [0,0,1,1,1,1,1,0]
        self.assertListEqual(output, Solution().prisonAfterNDays(cells, N))

    def test_prisonAfterNDays_2(self):
        cells = [1,1,0,1,1,0,1,1]
        N = 6
        output = [0,0,1,0,0,1,0,0]
        self.assertListEqual(output, Solution().prisonAfterNDays(cells, N))

    def test_prisonAfterNDays_3(self):
        cells = [0,0,0,1,1,0,1,0]
        N = 574
        output = [0,0,0,1,1,0,1,0]
        self.assertListEqual(output, Solution().prisonAfterNDays(cells, N))

