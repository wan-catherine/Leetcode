from unittest import TestCase
from problems.N1977_Number_Of_Ways_To_Separate_Numbers import Solution

class TestSolution(TestCase):
    def test_number_of_combinations(self):
        self.assertEqual(2, Solution().numberOfCombinations("327"))

    def test_number_of_combinations_1(self):
        self.assertEqual(0, Solution().numberOfCombinations("094"))

    def test_number_of_combinations_2(self):
        self.assertEqual(0, Solution().numberOfCombinations("0"))

    def test_number_of_combinations_3(self):
        self.assertEqual(101, Solution().numberOfCombinations("9999999999999"))

    def test_number_of_combinations_4(self):
        self.assertEqual(2, Solution().numberOfCombinations("1023"))
