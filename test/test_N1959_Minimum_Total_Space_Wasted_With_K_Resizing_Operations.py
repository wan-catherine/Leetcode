from unittest import TestCase
from problems.N1959_Minimum_Total_Space_Wasted_With_K_Resizing_Operations import Solution

class TestSolution(TestCase):
    def test_min_space_wasted_kresizing(self):
        self.assertEqual(10, Solution().minSpaceWastedKResizing(nums = [10,20], k = 0))

    def test_min_space_wasted_kresizing_1(self):
        self.assertEqual(10, Solution().minSpaceWastedKResizing(nums = [10,20,30], k = 1))

    def test_min_space_wasted_kresizing_2(self):
        self.assertEqual(15, Solution().minSpaceWastedKResizing(nums = [10,20,15,30,20], k = 2))

