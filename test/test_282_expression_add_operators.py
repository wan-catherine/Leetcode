from unittest import TestCase
from problems.N282_Expression_Add_Operators import Solution

class TestSolution(TestCase):
    def test_addOperators(self):
        self.assertListEqual(["1+2+3", "1*2*3"], Solution().addOperators(num = "123", target = 6))

    def test_addOperators_1(self):
        self.assertListEqual(["2+3*2", "2*3+2"], Solution().addOperators(num = "232", target = 8))

    def test_addOperators_2(self):
        self.assertListEqual(["1*0+5","10-5"], Solution().addOperators(num = "105", target = 5))

    def test_addOperators_3(self):
        self.assertListEqual(["0+0", "0-0", "0*0"], Solution().addOperators(num = "00", target = 0))

    def test_addOperators_4(self):
        self.assertListEqual([], Solution().addOperators(num = "3456237490", target = 9191))

