from unittest import TestCase
from problems.N1558_Minimum_Number_Of_Function_Calls_To_Make_Target_Array import Solution

class TestSolution(TestCase):
    def test_minOperations(self):
        self.assertEqual(5, Solution().minOperations([1,5]))

    def test_minOperations_1(self):
        self.assertEqual(3, Solution().minOperations([2,2]))

    def test_minOperations_2(self):
        self.assertEqual(6, Solution().minOperations([4,2,5]))

    def test_minOperations_3(self):
        self.assertEqual(7, Solution().minOperations([3,2,2,4]))

    def test_minOperations_4(self):
        self.assertEqual(8, Solution().minOperations([2,4,8,16]))