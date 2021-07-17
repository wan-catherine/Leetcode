from unittest import TestCase
from problems.N927_Three_Equal_Parts import Solution

class TestSolution(TestCase):
    def test_three_equal_parts(self):
        self.assertListEqual([0,3], Solution().threeEqualParts([1,0,1,0,1]))

    def test_three_equal_parts_1(self):
        self.assertListEqual([-1,-1], Solution().threeEqualParts([1,1,0,1,1]))

    def test_three_equal_parts_2(self):
        self.assertListEqual([0,2], Solution().threeEqualParts([1,1,0,0,1]))
