from unittest import TestCase
from problems.N1461_Check_If_A_String_Contains_All_Binary_Codes_Of_Size_K import Solution

class TestSolution(TestCase):
    def test_hasAllCodes(self):
        self.assertTrue(Solution().hasAllCodes(s = "00110110", k = 2))

    def test_hasAllCodes_1(self):
        self.assertTrue(Solution().hasAllCodes(s = "00110", k = 2))

    def test_hasAllCodes_2(self):
        self.assertTrue(Solution().hasAllCodes(s = "0110", k = 1))

    def test_hasAllCodes_3(self):
        self.assertFalse(Solution().hasAllCodes(s = "0110", k = 2))

    def test_hasAllCodes_4(self):
        self.assertFalse(Solution().hasAllCodes(s = "0000000001011100", k = 4))
