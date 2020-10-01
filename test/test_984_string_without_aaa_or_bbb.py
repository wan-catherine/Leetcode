from unittest import TestCase
from problems.N984_String_Without_AAA_Or_BBB import Solution

class TestSolution(TestCase):
    def test_strWithout3a3b(self):
        self.assertEqual("abb", Solution().strWithout3a3b(1, 2))

    def test_strWithout3a3b_1(self):
        self.assertEqual("aabaa", Solution().strWithout3a3b(4, 1))

    def test_strWithout3a3b_2(self):
        self.assertEqual("bbabbab", Solution().strWithout3a3b(2, 5))

