from unittest import TestCase
from problems.N394_Decode_String import Solution

class TestSolution(TestCase):
    def test_decodeString(self):
        self.assertEqual("aaabcbc", Solution().decodeString("3[a]2[bc]"))

    def test_decodeString_1(self):
        self.assertEqual("accaccacc", Solution().decodeString("3[a2[c]]"))

    def test_decodeString_2(self):
        self.assertEqual("abcabccdcdcdef", Solution().decodeString("2[abc]3[cd]ef"))

    def test_decodeString_3(self):
        self.assertEqual("abccdcdcdxyz", Solution().decodeString("abc3[cd]xyz"))
