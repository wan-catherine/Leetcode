from unittest import TestCase
from problems.N639_Decode_Ways_II import Solution

class TestSolution(TestCase):
    def test_num_decodings(self):
        self.assertEqual(9, Solution().numDecodings("*"))

    def test_num_decodings_1(self):
        self.assertEqual(18, Solution().numDecodings("1*"))

    def test_num_decodings_2(self):
        self.assertEqual(15, Solution().numDecodings("2*"))

    def test_num_decodings_3(self):
        self.assertEqual(0, Solution().numDecodings("0"))

    def test_num_decodings_4(self):
        self.assertEqual(180, Solution().numDecodings("*1*"))
