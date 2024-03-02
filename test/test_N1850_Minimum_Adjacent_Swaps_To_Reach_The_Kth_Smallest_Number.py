from unittest import TestCase
from problems.N1850_Minimum_Adjacent_Swaps_To_Reach_The_Kth_Smallest_Number import Solution

class TestSolution(TestCase):
    def test_get_min_swaps(self):
        self.assertEqual(2, Solution().getMinSwaps(num = "5489355142", k = 4))

    def test_get_min_swaps_1(self):
        self.assertEqual(4, Solution().getMinSwaps(num = "11112", k = 4))

    def test_get_min_swaps_2(self):
        self.assertEqual(1, Solution().getMinSwaps(num = "00123", k = 1))
