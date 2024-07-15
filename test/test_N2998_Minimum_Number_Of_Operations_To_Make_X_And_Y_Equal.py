from unittest import TestCase
from problems.N2998_Minimum_Number_Of_Operations_To_Make_X_And_Y_Equal import Solution

class TestSolution(TestCase):
    def test_minimum_operations_to_make_equal(self):
        self.assertEquals(3, Solution().minimumOperationsToMakeEqual(26, 1))

    def test_minimum_operations_to_make_equal_1(self):
        self.assertEquals(4, Solution().minimumOperationsToMakeEqual(54, 2))

    def test_minimum_operations_to_make_equal_2(self):
        self.assertEquals(5, Solution().minimumOperationsToMakeEqual(25, 30))

    def test_minimum_operations_to_make_equal_3(self):
        self.assertEquals(2, Solution().minimumOperationsToMakeEqual(4, 1))
