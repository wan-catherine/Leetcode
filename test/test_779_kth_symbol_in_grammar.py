from unittest import TestCase
from problems.N779_Kth_Symbol_In_Grammar import Solution

class TestSolution(TestCase):
    def test_kthGrammar(self):
        self.assertEqual(0, Solution().kthGrammar(1, 1))

    def test_kthGrammar_1(self):
        self.assertEqual(0, Solution().kthGrammar(2, 1))

    def test_kthGrammar_2(self):
        self.assertEqual(1, Solution().kthGrammar(2, 2))

    def test_kthGrammar_3(self):
        self.assertEqual(1, Solution().kthGrammar(4, 5))
