from unittest import TestCase
from problems.N1713_Minimum_Operations_To_Make_A_Subsequence import Solution

class TestSolution(TestCase):
    def test_minOperations(self):
        self.assertEqual(2, Solution().minOperations(target = [5,1,3], arr = [9,4,2,3,4]))

    def test_minOperations_1(self):
        self.assertEqual(3, Solution().minOperations(target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]))
