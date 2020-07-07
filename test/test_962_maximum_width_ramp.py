from unittest import TestCase
from problems.N962_Maximum_Width_Ramp import Solution

class TestSolution(TestCase):
    def test_maxWidthRamp(self):
        self.assertEqual(4, Solution().maxWidthRamp([6,0,8,2,1,5]))

    def test_maxWidthRamp_1(self):
        self.assertEqual(7, Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))