from unittest import TestCase
from problems.N665_Non_Decreasing_Array import Solution

class TestSolution(TestCase):
    def test_checkPossibility(self):
        self.assertTrue(Solution().checkPossibility([4,2,3]))

    def test_checkPossibility_1(self):
        self.assertFalse(Solution().checkPossibility([4,2,1]))

    def test_checkPossibility_2(self):
        self.assertFalse(Solution().checkPossibility([3,4,2,3]))

    def test_checkPossibility_3(self):
        self.assertTrue(Solution().checkPossibility([5,7,1,8]))

    def test_checkPossibility_4(self):
        self.assertTrue(Solution().checkPossibility([-1,4,2,3]))
