from unittest import TestCase
from problems.N423_Reconstruct_Original_Digits_From_English import Solution

class TestSolution(TestCase):
    def test_originalDigits(self):
        self.assertEqual("012", Solution().originalDigits("owoztneoer"))

    def test_originalDigits_1(self):
        self.assertEqual("45", Solution().originalDigits("fviefuro"))

    def test_originalDigits_2(self):
        self.assertEqual("3", Solution().originalDigits("ereht"))

    def test_originalDigits_3(self):
        self.assertEqual("9", Solution().originalDigits("nnei"))