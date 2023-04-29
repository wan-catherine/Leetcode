from unittest import TestCase
from problems.N2654_Minimum_Number_Of_Operations_To_Make_All_Array_Elements_Equal_To_1 import Solution

class TestSolution(TestCase):
    def test_min_operations(self):
        self.assertEqual(4, Solution().minOperations([2,6,3,4]))

    def test_min_operations_1(self):
        self.assertEqual(-1, Solution().minOperations([2,10,6,14]))

    def test_min_operations_2(self):
        self.assertEqual(-1, Solution().minOperations([410193,229980,600441]))

    def test_min_operations_3(self):
        self.assertEqual(4, Solution().minOperations([6,10,15]))

    def test_min_operations_4(self):
        self.assertEqual(5, Solution().minOperations([4,2,6,3]))

    def test_min_operations_5(self):
        self.assertEqual(0, Solution().minOperations([1,1]))

    def test_min_operations_6(self):
        self.assertEqual(1, Solution().minOperations([1,2]))

    def test_min_operations_7(self):
        self.assertEqual(13, Solution().minOperations([10,5,10,30,70,4,2,6,8,4]))