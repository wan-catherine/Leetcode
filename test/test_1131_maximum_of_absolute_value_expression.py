from unittest import TestCase
from problems.N1131_Maximum_Of_Absolute_Value_Expression import Solution

class TestSolution(TestCase):
    def test_maxAbsValExpr(self):
        self.assertEqual(13, Solution().maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6]))

    def test_maxAbsValExpr_1(self):
        self.assertEqual(20, Solution().maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))
