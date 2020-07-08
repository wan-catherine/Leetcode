from unittest import TestCase
from problems.N978_Longest_Turbulent_Subarray import Solution

class TestSolution(TestCase):
    def test_maxTurbulenceSize(self):
        self.assertEqual(5, Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))

    def test_maxTurbulenceSize_1(self):
        self.assertEqual(2, Solution().maxTurbulenceSize([4,8,12,16]))

    def test_maxTurbulenceSize_2(self):
        self.assertEqual(1, Solution().maxTurbulenceSize([100]))
