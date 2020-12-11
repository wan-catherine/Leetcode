from unittest import TestCase
from problems.N996_Number_Of_Squareful_Arrays import Solution

class TestSolution(TestCase):
    def test_numSquarefulPerms(self):
        self.assertEqual(2, Solution().numSquarefulPerms([1,17,8]))

    def test_numSquarefulPerms_1(self):
        self.assertEqual(1, Solution().numSquarefulPerms([2,2,2]))

    def test_numSquarefulPerms_2(self):
        self.assertEqual(6, Solution().numSquarefulPerms([2,2,7,7,2]))