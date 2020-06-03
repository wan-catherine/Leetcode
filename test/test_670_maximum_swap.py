from unittest import TestCase
from problems.N670_Maximum_Swap import Solution

class TestSolution(TestCase):
    def test_maximumSwap(self):
        self.assertEqual(7236, Solution().maximumSwap(2736))

    def test_maximumSwap_1(self):
        self.assertEqual(9973, Solution().maximumSwap(9973))

    def test_maximumSwap_2(self):
        self.assertEqual(511, Solution().maximumSwap(115))

    def test_maximumSwap_3(self):
        self.assertEqual(98863, Solution().maximumSwap(98368))

    def test_maximumSwap_4(self):
        self.assertEqual(9913, Solution().maximumSwap(1993))

