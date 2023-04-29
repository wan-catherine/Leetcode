from unittest import TestCase
from problems.N2658_Maximum_Number_Of_Fish_In_A_Grid import Solution

class TestSolution(TestCase):
    def test_find_max_fish(self):
        self.assertEqual(7, Solution().findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))

    def test_find_max_fish_1(self):
        self.assertEqual(1, Solution().findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))
