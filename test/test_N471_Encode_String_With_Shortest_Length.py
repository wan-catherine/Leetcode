from unittest import TestCase
from problems.N471_Encode_String_With_Shortest_Length import Solution

class TestSolution(TestCase):
    def test_encode(self):
        self.assertEqual("aaa", Solution().encode("aaa"))

    def test_encode_1(self):
        self.assertEqual("5[a]", Solution().encode("aaaaa"))

    def test_encode_2(self):
        self.assertEqual("10[a]", Solution().encode("aaaaaaaaaa"))

    def test_encode_3(self):
        self.assertEqual("2[aabc]d", Solution().encode("aabcaabcd"))

    def test_encode_4(self):
        self.assertEqual("2[2[abbb]c]", Solution().encode("abbbabbbcabbbabbbc"))
