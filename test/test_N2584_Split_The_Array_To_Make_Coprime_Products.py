from unittest import TestCase
from problems.N2584_Split_The_Array_To_Make_Coprime_Products import Solution

class TestSolution(TestCase):
    def test_find_valid_split(self):
        self.assertEqual(2, Solution().findValidSplit([4,7,8,15,3,5]))

    def test_find_valid_split_1(self):
        self.assertEqual(-1, Solution().findValidSplit([4,7,15,8,3,5]))