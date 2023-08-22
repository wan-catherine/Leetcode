from unittest import TestCase
from problems.N2826_Sorting_Three_Groups import Solution

class TestSolution(TestCase):
    def test_minimum_operations(self):
        self.assertEquals(3, Solution().minimumOperations([2,1,3,2,1]))

    def test_minimum_operations_1(self):
        self.assertEquals(2, Solution().minimumOperations([1,3,2,1,3,3]))

    def test_minimum_operations_2(self):
        self.assertEquals(0, Solution().minimumOperations([2,2,2,2,3,3]))
