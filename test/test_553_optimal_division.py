from unittest import TestCase
from problems.N553_Optimal_Division import Solution

class TestSolution(TestCase):
    def test_optimalDivision(self):
        self.assertEqual("1000/(100/10/2)", Solution().optimalDivision([1000,100,10,2]))


