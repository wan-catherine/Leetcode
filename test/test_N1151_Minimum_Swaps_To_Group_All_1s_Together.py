from unittest import TestCase
from problems.N1151_Minimum_Swaps_To_Group_All_1s_Together import Solution

class TestSolution(TestCase):
    def test_min_swaps(self):
        self.assertEqual(1, Solution().minSwaps([1,0,1,0,1]))

    def test_min_swaps_1(self):
        self.assertEqual(0, Solution().minSwaps([0,0,0,1,0]))

    def test_min_swaps_2(self):
        self.assertEqual(3, Solution().minSwaps([1,0,1,0,1,0,0,1,1,0,1]))

    def test_min_swaps_3(self):
        self.assertEqual(8, Solution().minSwaps([1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]))

    def test_min_swaps_4(self):
        self.assertEqual(30, Solution().minSwaps([1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]))

