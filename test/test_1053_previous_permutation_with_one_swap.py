from unittest import TestCase
from problems.N1053_Previous_Permutation_With_One_Swap import Solution

class TestSolution(TestCase):
    def test_prevPermOpt1(self):
        self.assertListEqual([3,1,2], Solution().prevPermOpt1([3,2,1]))

    def test_prevPermOpt1_1(self):
        self.assertListEqual([1,1,5], Solution().prevPermOpt1([1,1,5]))

    def test_prevPermOpt1_2(self):
        self.assertListEqual([1,7,4,6,9], Solution().prevPermOpt1([1,9,4,6,7]))

    def test_prevPermOpt1_3(self):
        self.assertListEqual([1,3,1,3], Solution().prevPermOpt1([3,1,1,3]))
