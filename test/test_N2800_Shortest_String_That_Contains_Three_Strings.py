from unittest import TestCase
from problems.N2800_Shortest_String_That_Contains_Three_Strings import Solution

class TestSolution(TestCase):
    def test_minimum_string(self):
        self.assertEquals("aaabca", Solution().minimumString(a = "abc", b = "bca", c = "aaa"))

    def test_minimum_string_1(self):
        self.assertEquals("aba", Solution().minimumString(a = "ab", b = "ba", c = "aba"))

    def test_minimum_string_2(self):
        self.assertEquals("ca", Solution().minimumString(a = "ca", b = "a", c = "a"))
