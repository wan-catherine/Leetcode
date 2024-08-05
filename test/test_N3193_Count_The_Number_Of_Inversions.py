from unittest import TestCase
from problems.N3193_Count_The_Number_Of_Inversions import Solution

class TestSolution(TestCase):
    def test_number_of_permutations(self):
        self.assertEquals(2, Solution().numberOfPermutations(n = 3, requirements = [[2,2],[0,0]]))

    def test_number_of_permutations_1(self):
        self.assertEquals(1, Solution().numberOfPermutations(n = 3, requirements = [[2,2],[1,1],[0,0]]))

    def test_number_of_permutations_2(self):
        self.assertEquals(1, Solution().numberOfPermutations(n = 2, requirements = [[0,0],[1,0]]))
