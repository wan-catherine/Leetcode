from unittest import TestCase
from problems.N823_Binary_Trees_With_Factors import Solution

class TestSolution(TestCase):
    def test_numFactoredBinaryTrees(self):
        self.assertEqual(3, Solution().numFactoredBinaryTrees([2, 4]))

    def test_numFactoredBinaryTrees_1(self):
        self.assertEqual(7, Solution().numFactoredBinaryTrees([2, 4, 5, 10]))

    def test_numFactoredBinaryTrees_2(self):
        self.assertEqual(777, Solution().numFactoredBinaryTrees([45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]))
