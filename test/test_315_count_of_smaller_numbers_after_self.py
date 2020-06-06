from unittest import TestCase
from problems.N315_Count_Of_Smaller_Numbers_After_Self import Solution

class TestSolution(TestCase):
    def test_countSmaller(self):
        self.assertListEqual([2,1,1,0], Solution().countSmaller([5,2,6,1]))

    def test_countSmaller_1(self):
        self.assertListEqual([0,0], Solution().countSmaller([-1,-1]))
