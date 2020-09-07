from unittest import TestCase
from problems.N1529_Bulb_Switcher_IV import Solution

class TestSolution(TestCase):
    def test_minFlips(self):
        self.assertEqual(3, Solution().minFlips("10111"))

    def test_minFlips_1(self):
        self.assertEqual(3, Solution().minFlips("101"))

    def test_minFlips_2(self):
        self.assertEqual(0, Solution().minFlips("00000"))

    def test_minFlips_3(self):
        self.assertEqual(5, Solution().minFlips("001011101"))
