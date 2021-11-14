from unittest import TestCase
from problems.N945_Minimum_Increment_To_Make_Array_Unique import Solution

class TestSolution(TestCase):
    def test_minIncrementForUnique(self):
        self.assertEqual(1, Solution().minIncrementForUnique([1,2,2]))

    def test_minIncrementForUnique_1(self):
        self.assertEqual(6, Solution().minIncrementForUnique([3,2,1,2,1,7]))

    def test_minIncrementForUnique_2(self):
        self.assertEqual(3, Solution().minIncrementForUnique([2,2,2,1]))

