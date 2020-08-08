from unittest import TestCase
from problems.N1541_Minimum_Insertions_To_Balance_A_Parentheses_String import Solution

class TestSolution(TestCase):
    def test_minInsertions(self):
        s = "(()))"
        self.assertEqual(1, Solution().minInsertions(s))

    def test_minInsertions_1(self):
        s = "())"
        self.assertEqual(0, Solution().minInsertions(s))

    def test_minInsertions_2(self):
        s = "))())("
        self.assertEqual(3, Solution().minInsertions(s))

    def test_minInsertions_3(self):
        s = "(((((("
        self.assertEqual(12, Solution().minInsertions(s))

    def test_minInsertions_4(self):
        s = ")))))))"
        self.assertEqual(5, Solution().minInsertions(s))

    def test_minInsertions_5(self):
        s = "()()()()()("
        self.assertEqual(7, Solution().minInsertions(s))

    def test_minInsertions_6(self):
        s = "(()))(()))()())))"
        self.assertEqual(4, Solution().minInsertions(s))

    def test_minInsertions_7(self):
        s = "(((()(()((())))(((()())))()())))(((()(()()((()()))"
        self.assertEqual(31, Solution().minInsertions(s))