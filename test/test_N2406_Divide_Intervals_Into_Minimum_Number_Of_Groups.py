from unittest import TestCase
from problems.N2406_Divide_Intervals_Into_Minimum_Number_Of_Groups import Solution

class TestSolution(TestCase):
    def test_min_groups(self):
        self.assertEqual(3, Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))

    def test_min_groups_1(self):
        self.assertEqual(1, Solution().minGroups([[1,3],[5,6],[8,10],[11,13]]))
