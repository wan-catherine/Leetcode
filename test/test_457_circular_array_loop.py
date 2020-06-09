from unittest import TestCase
from problems.N457_Circular_Array_Loop import Solution

class TestSolution(TestCase):
    def test_circularArrayLoop(self):
        self.assertTrue(Solution().circularArrayLoop([2,-1,1,2,2]))

    def test_circularArrayLoop_1(self):
        self.assertFalse(Solution().circularArrayLoop([-1,2]))

    def test_circularArrayLoop_2(self):
        self.assertFalse(Solution().circularArrayLoop([-2,1,-1,-2,-2]))