from unittest import TestCase
from others.Get_Max_Matrix import Solution

class TestSolution(TestCase):
    def test_getMaxMatrix(self):
        self.assertListEqual([0,0,2,3], Solution().getMaxMatrix([[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]))

    def test_getMaxMatrix_1(self):
        self.assertListEqual([0,0,0,0], Solution().getMaxMatrix([[-4, -5]]))