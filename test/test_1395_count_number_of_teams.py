from unittest import TestCase
from problems.N1395_Count_Number_Of_Teams import Solution

class TestSolution(TestCase):
    def test_numTeams(self):
        self.assertEqual(3, Solution().numTeams([2,5,3,4,1]))

    def test_numTeams_1(self):
        self.assertEqual(0, Solution().numTeams([2,1,3]))

    def test_numTeams_2(self):
        self.assertEqual(4, Solution().numTeams([1,2,3,4]))
