from unittest import TestCase
from problems.N2772_Apply_Operations_To_Make_All_Array_Elements_Equal_To_Zero import Solution

class TestSolution(TestCase):
    def test_check_array(self):
        self.assertTrue(Solution().checkArray(nums = [2,2,3,1,1,0], k = 3))

    def test_check_array_1(self):
        self.assertFalse(Solution().checkArray(nums = [1,3,1,1], k = 2))
