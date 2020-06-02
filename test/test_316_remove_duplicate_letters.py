from unittest import TestCase
from problems.N316_Remove_Duplicate_Letters import Solution

class TestSolution(TestCase):
    def test_removeDuplicateLetters(self):
        self.assertEqual("abc", Solution().removeDuplicateLetters("bcabc"))

    def test_removeDuplicateLetters_1(self):
        self.assertEqual("acdb", Solution().removeDuplicateLetters("cbacdcbc"))

    def test_removeDuplicateLetters_2(self):
        self.assertEqual("adbc", Solution().removeDuplicateLetters("cdadabcc"))

    def test_removeDuplicateLetters_3(self):
        self.assertEqual("abcd", Solution().removeDuplicateLetters("abcd"))

    def test_removeDuplicateLetters_4(self):
        self.assertEqual("eacb", Solution().removeDuplicateLetters("ecbacba"))

    def test_removeDuplicateLetters_5(self):
        self.assertEqual("letcod", Solution().removeDuplicateLetters("leetcode"))

    def test_removeDuplicateLetters_6(self):
        self.assertEqual("abc", Solution().removeDuplicateLetters("abacb"))

    def test_removeDuplicateLetters_7(self):
        self.assertEqual("bca", Solution().removeDuplicateLetters("bcbcbcababa"))
