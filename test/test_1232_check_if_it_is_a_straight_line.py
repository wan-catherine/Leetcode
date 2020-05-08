from unittest import TestCase
from problems.N1232_Check_If_It_Is_A_Straight_Line import Solution

class TestSolution(TestCase):
    def test_checkStraightLine(self):
        self.assertEqual(True, Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))

    def test_checkStraightLine_1(self):
        self.assertEqual(False, Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))

    def test_checkStraightLine_2(self):
        self.assertEqual(False, Solution().checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))
