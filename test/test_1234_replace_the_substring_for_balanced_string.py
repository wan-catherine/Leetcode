from unittest import TestCase
from problems.N1234_Replace_The_Subtring_For_Balanced_String import Solution

class TestSolution(TestCase):
    def test_balancedString(self):
        self.assertEqual(0, Solution().balancedString("QWER"))

    def test_balancedString_1(self):
        self.assertEqual(1, Solution().balancedString("QQWE"))

    def test_balancedString_2(self):
        self.assertEqual(2, Solution().balancedString("QQQW"))

    def test_balancedString_3(self):
        self.assertEqual(3, Solution().balancedString("QQQQ"))

    def test_balancedString_4(self):
        self.assertEqual(4, Solution().balancedString("WWQQRRRRQRQQ"))

    def test_balancedString_5(self):
        self.assertEqual(3, Solution().balancedString("WQWRQQQW"))
