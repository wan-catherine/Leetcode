from unittest import TestCase
from problems.N990_Satisfiability_Of_Equality_Equations import Solution

class TestSolution(TestCase):
    def test_equationsPossible(self):
        self.assertFalse(Solution().equationsPossible(["a==b","b!=a"]))

    def test_equationsPossible_1(self):
        self.assertTrue(Solution().equationsPossible(["b==a","a==b"]))

    def test_equationsPossible_2(self):
        self.assertTrue(Solution().equationsPossible(["a==b","b==c","a==c"]))

    def test_equationsPossible_3(self):
        self.assertFalse(Solution().equationsPossible(["a==b","b!=c","c==a"]))

    def test_equationsPossible_4(self):
        self.assertTrue(Solution().equationsPossible(["c==c","b==d","x!=z"]))

