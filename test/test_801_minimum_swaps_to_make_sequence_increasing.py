from unittest import TestCase
from problems.N801_Minimum_Swaps_To_Make_Sequences_Increasing import Solution

class TestSolution(TestCase):
    def test_minSwap(self):
        self.assertEqual(1, Solution().minSwap(A = [1,3,5,4], B = [1,2,3,7]))
