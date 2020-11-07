from unittest import TestCase
from problems.N330_Patching_Array import Solution

class TestSolution(TestCase):
    def test_minPatches(self):
        self.assertEqual(1, Solution().minPatches(nums = [1,3], n = 6))

    def test_minPatches_1(self):
        self.assertEqual(2, Solution().minPatches(nums = [1,5,10], n = 20))

    def test_minPatches_2(self):
        self.assertEqual(0, Solution().minPatches(nums = [1,2,2], n = 5))

    def test_minPatches_3(self):
        self.assertEqual(4, Solution().minPatches(nums = [], n = 8))