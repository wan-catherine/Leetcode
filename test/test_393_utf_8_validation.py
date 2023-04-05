from unittest import TestCase
from problems.N393_UTF_8_Validation import Solution

class TestSolution(TestCase):
    def test_validUtf8(self):
        self.assertTrue(Solution().validUtf8([197, 130, 1]))

    def test_validUtf8_1(self):
        self.assertFalse(Solution().validUtf8([235, 140, 4]))

    def test_validUtf8_2(self):
        self.assertFalse(Solution().validUtf8([145]))

    def test_validUtf8_3(self):
        self.assertFalse(Solution().validUtf8([248,130,130,130]))

    def test_validUtf8_4(self):
        self.assertTrue(Solution().validUtf8([115,100,102,231,154,132,13,10]))
