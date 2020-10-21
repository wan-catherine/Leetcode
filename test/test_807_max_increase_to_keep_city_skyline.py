from unittest import TestCase
from problems.N807_Max_Increase_To_Keep_City_Skyline import Solution

class TestSolution(TestCase):
    def test_maxIncreaseKeepingSkyline(self):
        self.assertEqual(35, Solution().maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
