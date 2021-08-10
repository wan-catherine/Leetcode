from unittest import TestCase
from problems.N1963_Minimum_Number_Of_Swaps_To_Make_The_String_Balanced import Solution

class TestSolution(TestCase):
    def test_min_swaps(self):
        self.assertEqual(1, Solution().minSwaps("][]["))

    def test_min_swaps_1(self):
        self.assertEqual(2, Solution().minSwaps("]]][[["))

    def test_min_swaps_2(self):
        self.assertEqual(0, Solution().minSwaps("[]"))
