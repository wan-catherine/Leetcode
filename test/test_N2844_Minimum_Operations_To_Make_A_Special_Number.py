from unittest import TestCase
from problems.N2844_Minimum_Operations_To_Make_A_Special_Number import Solution

class TestSolution(TestCase):
    def test_minimum_operations(self):
        self.assertEquals(2, Solution().minimumOperations("2245047"))

    def test_minimum_operations_1(self):
        self.assertEquals(3, Solution().minimumOperations("2908305"))

    def test_minimum_operations_2(self):
        self.assertEquals(1, Solution().minimumOperations("10"))
