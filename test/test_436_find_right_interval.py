from unittest import TestCase
from problems.N436_Find_Right_Interval import Solution

class TestSolution(TestCase):
    def test_findRightInterval(self):
        self.assertListEqual([-1], Solution().findRightInterval([[1,2]]))

    def test_findRightInterval_1(self):
        self.assertListEqual([-1, 2, -1], Solution().findRightInterval([[1,4], [2,3], [3,4]]))

    def test_findRightInterval_2(self):
        self.assertListEqual([-1, 0, 1], Solution().findRightInterval([[3,4], [2,3], [1,2]]))
