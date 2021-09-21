from unittest import TestCase
from problems.N2009_Minimum_Number_Of_Operations_To_Make_Array_Continuous import Solution

class TestSolution(TestCase):
    def test_min_operations(self):
        self.assertEqual(0, Solution().minOperations([4,2,5,3]))

    def test_min_operations_1(self):
        self.assertEqual(1, Solution().minOperations([1,2,3,5,6]))

    def test_min_operations_2(self):
        self.assertEqual(3, Solution().minOperations([1,10,100,1000]))
