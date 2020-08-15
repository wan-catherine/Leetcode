from unittest import TestCase
from problems.N845_Longest_Mountain_In_Array import Solution

class TestSolution(TestCase):
    def test_longestMountain(self):
        self.assertEqual(5, Solution().longestMountain([2,1,4,7,3,2,5]))

    def test_longestMountain_1(self):
        self.assertEqual(0, Solution().longestMountain([2,2,2]))

    def test_longestMountain_2(self):
        self.assertEqual(11, Solution().longestMountain([0,1,2,3,4,5,4,3,2,1,0]))

    def test_longestMountain_3(self):
        self.assertEqual(0, Solution().longestMountain([0,1,2,3,4,5,6,7,8,9]))

    def test_longestMountain_4(self):
        self.assertEqual(0, Solution().longestMountain([2,3,3,2,0,2]))
