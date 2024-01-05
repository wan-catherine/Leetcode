from unittest import TestCase
from problems.N2862_Maximum_Element_Sum_Of_A_Complete_Subset_Of_Indices import Solution

class TestSolution(TestCase):
    def test_maximum_sum(self):
        self.assertEqual(16, Solution().maximumSum([8,7,3,5,7,2,4,9]))

    def test_maximum_sum_1(self):
        self.assertEqual(19, Solution().maximumSum([5,10,3,10,1,13,7,9,4]))

    def test_maximum_sum_2(self):
        self.assertEqual(100, Solution().maximumSum([1,100,100,1]))

    def test_maximum_sum_3(self):
        self.assertEqual(1000000000, Solution().maximumSum([1,1,1000000000,1]))

    def test_maximum_sum_4(self):
        self.assertEqual(64, Solution().maximumSum([23,27,42,3,33,36,43,32,27,48,40,22,5,36,48]))
