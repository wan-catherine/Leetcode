from unittest import TestCase
from problems.N452_Minimum_Number_Of_Arrows_To_Burst_Balloons import Solution

class TestSolution(TestCase):
    def test_findMinArrowShots(self):
        self.assertEqual(2, Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
