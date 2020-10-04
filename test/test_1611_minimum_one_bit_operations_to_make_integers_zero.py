from unittest import TestCase
from problems.N1611_Minimum_One_Bit_Operations_To_Make_Integers_Zero import Solution

class TestSolution(TestCase):
    def test_minimumOneBitOperations(self):
        self.assertEqual(0, Solution().minimumOneBitOperations(0))

    def test_minimumOneBitOperations_1(self):
        self.assertEqual(2, Solution().minimumOneBitOperations(3))

    def test_minimumOneBitOperations_2(self):
        self.assertEqual(4, Solution().minimumOneBitOperations(6))

    def test_minimumOneBitOperations_3(self):
        self.assertEqual(14, Solution().minimumOneBitOperations(9))

    def test_minimumOneBitOperations_4(self):
        self.assertEqual(393, Solution().minimumOneBitOperations(333))