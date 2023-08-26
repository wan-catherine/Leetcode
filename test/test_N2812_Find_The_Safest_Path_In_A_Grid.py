from unittest import TestCase
from problems.N2812_Find_The_Safest_Path_In_A_Grid import Solution

class TestSolution(TestCase):
    def test_maximum_safeness_factor(self):
        self.assertEquals(0, Solution().maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))

    def test_maximum_safeness_factor_1(self):
        self.assertEquals(2, Solution().maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))

    def test_maximum_safeness_factor_2(self):
        self.assertEquals(2, Solution().maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))

    def test_maximum_safeness_factor_3(self):
        self.assertEquals(1, Solution().maximumSafenessFactor([[0,1,1],[0,0,0],[0,0,0]]))
