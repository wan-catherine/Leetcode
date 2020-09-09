from unittest import TestCase
from problems.N132_Palindrome_Partitioning_II import Solution

class TestSolution(TestCase):
    def test_minCut(self):
        self.assertEqual(1, Solution().minCut("aab"))

    def test_minCut_1(self):
        self.assertEqual(0, Solution().minCut("a"))

    def test_minCut_2(self):
        self.assertEqual(1, Solution().minCut("ab"))

    def test_minCut_3(self):
        self.assertEqual(0, Solution().minCut("ababababababababababababcbabababababababababababa"))

    def test_minCut_4(self):
        self.assertEqual(2, Solution().minCut("leet"))
