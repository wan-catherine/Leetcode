from unittest import TestCase
from problems.N1955_Count_Number_Of_Special_Subsequences import Solution

class TestSolution(TestCase):
    def test_count_special_subsequences(self):
        self.assertEqual(3, Solution().countSpecialSubsequences([0,1,2,2]))

    def test_count_special_subsequences_1(self):
        self.assertEqual(0, Solution().countSpecialSubsequences([2,2,0,0]))

    def test_count_special_subsequences_2(self):
        self.assertEqual(7, Solution().countSpecialSubsequences([0,1,2,0,1,2]))
