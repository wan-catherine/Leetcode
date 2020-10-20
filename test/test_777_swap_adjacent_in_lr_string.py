from unittest import TestCase
from problems.N777_Swap_Adjacent_In_LR_String import Solution

class TestSolution(TestCase):
    def test_canTransform(self):
        self.assertTrue(Solution().canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))

    def test_canTransform_1(self):
        self.assertFalse(Solution().canTransform(start = "X", end = "L"))

    def test_canTransform_2(self):
        self.assertFalse(Solution().canTransform(start = "LLR", end = "RRL"))

    def test_canTransform_3(self):
        self.assertTrue(Solution().canTransform(start = "XL", end = "LX"))

    def test_canTransform_4(self):
        self.assertFalse(Solution().canTransform(start = "XLLR", end = "LXLX"))

    def test_canTransform_5(self):
        self.assertFalse(Solution().canTransform("LXXLXRLXXL", "XLLXRXLXLX"))