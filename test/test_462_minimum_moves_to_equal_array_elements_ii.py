from unittest import TestCase
from problems.N462_Minimum_Moves_To_Equal_Array_Elements_II import Solution

class TestSolution(TestCase):
    def test_minMoves2(self):
        self.assertEqual(2, Solution().minMoves2([1,2,3]))
