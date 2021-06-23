from unittest import TestCase
from problems.N1896_Minimum_Cost_To_Change_The_Final_Value_Of_Expression import Solution

class TestSolution(TestCase):
    def test_min_operations_to_flip(self):
        self.assertEqual(1, Solution().minOperationsToFlip("1&(0|1)"))

    def test_min_operations_to_flip_(self):
        self.assertEqual(3, Solution().minOperationsToFlip("(0&0)&(0&0&0)"))

    def test_min_operations_to_flip_2(self):
        self.assertEqual(1, Solution().minOperationsToFlip("(0|(1|0&1))"))
