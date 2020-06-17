from unittest import TestCase
from problems.N130_Surrounded_Regions import Solution

class TestSolution(TestCase):
    def test_solve(self):
        self.assertListEqual([["O","O","O"],["O","O","O"],["O","O","O"]], Solution().solve([["O","O","O"],["O","O","O"],["O","O","O"]]))

    def test_solve_1(self):
        input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        self.assertListEqual([["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]], Solution().solve(input))

    def test_solve_2(self):
        input = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
        expected = [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
        self.assertListEqual(expected, Solution().solve(input))

