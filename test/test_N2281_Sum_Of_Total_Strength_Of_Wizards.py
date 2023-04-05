from unittest import TestCase
from problems.N2281_Sum_Of_Total_Strength_Of_Wizards import Solution

class TestSolution(TestCase):
    def test_total_strength(self):
        self.assertEqual(44, Solution().totalStrength([1,3,1,2]))

    def test_total_strength_1(self):
        self.assertEqual(213, Solution().totalStrength([5,4,6]))