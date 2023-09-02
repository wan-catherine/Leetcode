from unittest import TestCase
from problems.N2801_Count_Stepping_Numbers_In_Range import Solution

class TestSolution(TestCase):
    def test_count_stepping_numbers(self):
        self.assertEquals(10, Solution().countSteppingNumbers(low = "1", high = "11"))

    def test_count_stepping_numbers_1(self):
        self.assertEquals(2, Solution().countSteppingNumbers(low = "90", high = "101"))

    def test_count_stepping_numbers_2(self):
        self.assertEquals(1, Solution().countSteppingNumbers(low = "106", high = "121"))
