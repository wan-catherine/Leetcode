from unittest import TestCase
from problems.N537_Complex_Number_Multiplication import Solution

class TestSolution(TestCase):
    def test_complexNumberMultiply(self):
        self.assertEqual("0+2i", Solution().complexNumberMultiply("1+1i", "1+1i"))

    def test_complexNumberMultiply_1(self):
        self.assertEqual("0+-2i", Solution().complexNumberMultiply("1+-1i", "1+-1i"))
