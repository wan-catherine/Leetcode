from unittest import TestCase
from problems.N991_Broken_Calculator import Solution

class TestSolution(TestCase):
    def test_brokenCalc(self):
        self.assertEqual(2, Solution().brokenCalc(2, 3))

    def test_brokenCalc_1(self):
        self.assertEqual(2, Solution().brokenCalc(5, 8))

    def test_brokenCalc_2(self):
        self.assertEqual(3, Solution().brokenCalc(3, 10))

    def test_brokenCalc_3(self):
        self.assertEqual(1023, Solution().brokenCalc(1024, 1))

    def test_brokenCalc_4(self):
        self.assertEqual(39, Solution().brokenCalc(1, 1000000000))

    def test_brokenCalc_4(self):
        self.assertEqual(34, Solution().brokenCalc(68, 71))
