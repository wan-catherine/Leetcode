from unittest import TestCase
from problems.N1671_Minimum_Number_Of_Removals_To_Make_Mountain_Array import Solution

class TestSolution(TestCase):
    def test_minimumMountainRemovals(self):
        self.assertEqual(0, Solution().minimumMountainRemovals([1,3,1]))

    def test_minimumMountainRemovals_1(self):
        self.assertEqual(3, Solution().minimumMountainRemovals([2,1,1,5,6,2,3,1]))

    def test_minimumMountainRemovals_2(self):
        self.assertEqual(4, Solution().minimumMountainRemovals([4,3,2,1,1,2,3,1]))

    def test_minimumMountainRemovals_3(self):
        self.assertEqual(1, Solution().minimumMountainRemovals([1,2,3,4,4,3,2,1]))
