from unittest import TestCase
from problems.N2999_Count_The_Number_Of_Powerful_Integers import Solution

class TestSolution(TestCase):
    def test_number_of_powerful_int(self):
        self.assertEquals(5, Solution().numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"))

    def test_number_of_powerful_int_1(self):
        self.assertEquals(2, Solution().numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10"))

    def test_number_of_powerful_int_2(self):
        self.assertEquals(0, Solution().numberOfPowerfulInt(start = 1000, finish = 2000, limit = 4, s = "3000"))