from unittest import TestCase
from problems.N1593_Split_A_String_Into_The_Max_Number_Of_Unique_Substrings import Solution

class TestSolution(TestCase):
    def test_max_unique_split(self):
        self.assertEquals(5, Solution().maxUniqueSplit("ababccc"))

    def test_max_unique_split_1(self):
        self.assertEquals(2, Solution().maxUniqueSplit("aba"))

    def test_max_unique_split(self):
        self.assertEquals(1, Solution().maxUniqueSplit("aa"))
