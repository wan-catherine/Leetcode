from unittest import TestCase
from problems.N2659_Make_Arrary_Empty import Solution

class TestSolution(TestCase):
    def test_count_operations_to_empty_array(self):
        self.assertEqual(5, Solution().countOperationsToEmptyArray([3,4,-1]))

    def test_count_operations_to_empty_array_1(self):
        self.assertEqual(5, Solution().countOperationsToEmptyArray([1,2,4,3]))

    def test_count_operations_to_empty_array_2(self):
        self.assertEqual(3, Solution().countOperationsToEmptyArray([1,2,3]))
