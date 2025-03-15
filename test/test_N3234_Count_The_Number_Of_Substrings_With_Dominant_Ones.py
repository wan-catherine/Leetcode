from unittest import TestCase
from problems.N3234_Count_The_Number_Of_Substrings_With_Dominant_Ones import Solution

class TestSolution(TestCase):
    def test_number_of_substrings(self):
        self.assertEquals(5, Solution().numberOfSubstrings("00011"))

    def test_number_of_substrings_1(self):
        self.assertEquals(16, Solution().numberOfSubstrings("101101"))
