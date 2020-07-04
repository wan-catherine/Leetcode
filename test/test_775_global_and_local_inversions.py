from unittest import TestCase
from problems.N775_Global_And_Local_Inversions import Solution

class TestSolution(TestCase):
    def test_isIdealPermutation(self):
        self.assertTrue(Solution().isIdealPermutation([1,0,2]))

    def test_isIdealPermutation_1(self):
        self.assertFalse(Solution().isIdealPermutation([1,2,0]))
