from unittest import TestCase
from problems.N315_Count_Of_Smaller_Numbers_After_Self import Solution

class TestSolution(TestCase):
    def test_countSmaller(self):
        self.assertListEqual([2,1,1,0], Solution().countSmaller([5,2,6,1]))

    def test_countSmaller_1(self):
        self.assertListEqual([0,0], Solution().countSmaller([-1,-1]))

    def test_countSmaller_2(self):
        self.assertListEqual([0,3,1,1,0], Solution().countSmaller([1,9,7,8,5]))

    def test_countSmaller_3(self):
        self.assertListEqual([10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0], Solution().countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))
