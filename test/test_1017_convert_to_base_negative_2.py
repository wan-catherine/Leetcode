from unittest import TestCase
from problems.N1017_Convert_To_Base_Negative_2 import Solution

class TestSolution(TestCase):
    def test_baseNeg2(self):
        self.assertEqual("110", Solution().baseNeg2(2))

    def test_baseNeg2_1(self):
        self.assertEqual("111", Solution().baseNeg2(3))

    def test_baseNeg2_2(self):
        self.assertEqual("100", Solution().baseNeg2(4))

