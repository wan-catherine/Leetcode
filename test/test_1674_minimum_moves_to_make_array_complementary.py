from unittest import TestCase
from problems.N1674_Minimum_Moves_To_Make_Array_Complementary import Solution

class TestSolution(TestCase):
    def test_minMoves(self):
        self.assertEqual(1, Solution().minMoves(nums = [1,2,4,3], limit = 4))

    def test_minMoves_1(self):
        self.assertEqual(2, Solution().minMoves(nums = [1,2,2,1], limit = 2))

    def test_minMoves_2(self):
        self.assertEqual(0, Solution().minMoves(nums = [1,2,1,2], limit = 2))
