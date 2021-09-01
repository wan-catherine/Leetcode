from unittest import TestCase
from problems.N640_Solve_The_Equation import Solution

class TestSolution(TestCase):
    def test_solve_equation(self):
        self.assertEqual("x=2", Solution().solveEquation("x+5-3+x=6+x-2"))

    def test_solve_equation_1(self):
        self.assertEqual("Infinite solutions", Solution().solveEquation("x=x"))

    def test_solve_equation_2(self):
        self.assertEqual("x=0", Solution().solveEquation("2x=x"))

    def test_solve_equation_3(self):
        self.assertEqual("x=-1", Solution().solveEquation("2x+3x-6x=x+2"))

    def test_solve_equation_4(self):
        self.assertEqual("No solution", Solution().solveEquation("x=x+2"))

    def test_solve_equation_5(self):
        self.assertEqual("Infinite solutions", Solution().solveEquation("0x=0"))
