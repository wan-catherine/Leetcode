from unittest import TestCase
from problems.N1130_Minimum_Cost_Tree_From_Leaf_Values import Solution

class TestSolution(TestCase):
    def test_mctFromLeafValues(self):
        self.assertEqual(32, Solution().mctFromLeafValues([6,2,4]))

    def test_mctFromLeafValues_1(self):
        self.assertEqual(44, Solution().mctFromLeafValues([4,11]))
