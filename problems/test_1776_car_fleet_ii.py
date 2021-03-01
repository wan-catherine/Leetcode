from unittest import TestCase
from problems.N1776_Car_Fleet_II import Solution

class TestSolution(TestCase):
    def test_getCollisionTimes(self):
        self.assertListEqual([1.00000,-1.00000,3.00000,-1.00000], Solution().getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))

    def test_getCollisionTimes_1(self):
        self.assertListEqual([2.00000,1.00000,1.50000,-1.00000], Solution().getCollisionTimes([[3,4],[5,4],[6,3],[9,1]]))
