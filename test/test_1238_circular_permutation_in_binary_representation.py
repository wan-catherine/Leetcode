from unittest import TestCase
from problems.N1238_Circular_Permutation_In_Binary_Representation import Solution

class TestSolution(TestCase):
    def test_circularPermutation(self):
        self.assertListEqual([3,2,0,1], Solution().circularPermutation(2, 3))

    def test_circularPermutation_1(self):
        self.assertListEqual([2,6,7,5,4,0,1,3], Solution().circularPermutation(3, 2))
