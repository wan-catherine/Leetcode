from unittest import TestCase
from problems.N1201_Ugly_Number_III import Solution

class TestSolution(TestCase):
    def test_nthUglyNumber(self):
        n = 3
        a = 2
        b = 3
        c = 5
        self.assertEqual(4, Solution().nthUglyNumber(n,a,b,c))

    def test_nthUglyNumber_1(self):
        self.assertEqual(6, Solution().nthUglyNumber(4,2,3,4))

    def test_nthUglyNumber_2(self):
        self.assertEqual(10, Solution().nthUglyNumber(5,2,11,13))

    def test_nthUglyNumber_3(self):
        self.assertEqual(1999999984, Solution().nthUglyNumber(1000000000,2,217983653,336916467))
