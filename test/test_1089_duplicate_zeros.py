from unittest import TestCase
from problems.N1089_Duplicate_zeros import Solution

class TestSolution(TestCase):
    def test_duplicateZeros(self):
        input = [1,0,2,3,0,4,5,0]
        Solution().duplicateZeros(input)
        self.assertListEqual([1,0,0,2,3,0,0,4], input)

    def test_duplicateZeros_1(self):
        input = [1,2,3]
        Solution().duplicateZeros(input)
        self.assertListEqual([1,2,3], input)

    def test_duplicateZeros_2(self):
        input = [1,5,2,0,6,8,0,6,0]
        Solution().duplicateZeros(input)
        self.assertListEqual([1,5,2,0,0,6,8,0,0], input)