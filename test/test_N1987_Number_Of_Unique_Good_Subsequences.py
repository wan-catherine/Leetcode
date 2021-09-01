from unittest import TestCase
from problems.N1987_Number_Of_Unique_Good_Subsequences import Solution

class TestSolution(TestCase):
    def test_number_of_unique_good_subsequences(self):
        self.assertEqual(2, Solution().numberOfUniqueGoodSubsequences("001"))

    def test_number_of_unique_good_subsequences_1(self):
        self.assertEqual(2, Solution().numberOfUniqueGoodSubsequences("11"))

    def test_number_of_unique_good_subsequences_2(self):
        self.assertEqual(5, Solution().numberOfUniqueGoodSubsequences("101"))
