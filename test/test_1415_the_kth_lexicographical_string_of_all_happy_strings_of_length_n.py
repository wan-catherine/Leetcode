from unittest import TestCase
from problems.N1415_The_Kth_Lexicographical_String_Of_All_Happy_Strings_Of_Length_N import Solution

class TestSolution(TestCase):
    def test_getHappyString(self):
        self.assertEqual("c", Solution().getHappyString(n = 1, k = 3))

    def test_getHappyString_1(self):
        self.assertEqual("", Solution().getHappyString(1, 4))

    def test_getHappyString_2(self):
        self.assertEqual("cab", Solution().getHappyString(3, 9))

    def test_getHappyString_3(self):
        self.assertEqual("", Solution().getHappyString(2, 7))

    def test_getHappyString_4(self):
        self.assertEqual("abacbabacb", Solution().getHappyString(10, 100))
