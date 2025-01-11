from unittest import TestCase
from problems.N3404_Count_Special_Subsequences import Solution

class TestSolution(TestCase):
    def test_number_of_subsequences(self):
        self.assertEquals(1, Solution().numberOfSubsequences([1,2,3,4,3,6,1]))

    def test_number_of_subsequences_1(self):
        self.assertEquals(3, Solution().numberOfSubsequences([3,4,3,4,3,4,3,4]))
