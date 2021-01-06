from unittest import TestCase
from problems.N960_Delete_Columns_To_Make_Sorted_III import Solution

class TestSolution(TestCase):
    def test_minDeletionSize(self):
        self.assertEqual(3, Solution().minDeletionSize(["babca","bbazb"]))

    def test_minDeletionSize_1(self):
        self.assertEqual(4, Solution().minDeletionSize(["edcba"]))

    def test_minDeletionSize_2(self):
        self.assertEqual(0, Solution().minDeletionSize(["ghi","def","abc"]))
