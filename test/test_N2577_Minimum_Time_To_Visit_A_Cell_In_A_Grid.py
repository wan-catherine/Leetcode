from unittest import TestCase
from problems.N2577_Minimum_Time_To_Visit_A_Cell_In_A_Grid import Solution

class TestSolution(TestCase):
    def test_minimum_time(self):
        self.assertEquals(7, Solution().minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]]))

    def test_minimum_time_1(self):
        self.assertEquals(-1, Solution().minimumTime([[0,2,4],[3,2,1],[1,0,4]]))
