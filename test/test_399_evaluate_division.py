from unittest import TestCase
from problems.N399_Evaluate_Division import Solution

class TestSolution(TestCase):
    def test_calcEquation(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        self.assertListEqual([6.0, 0.5, -1.0, 1.0, -1.0 ], Solution().calcEquation(equations, values, queries))

    def test_calcEquation_1(self):
        equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
        values = [3.0, 4.0, 5.0, 6.0]
        queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
        self.assertListEqual([360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000], Solution().calcEquation(equations, values, queries))
