from unittest import TestCase
from problems.N2434_Using_A_Robot_To_Print_The_Lexicographically_Smallest_String import Solution

class TestSolution(TestCase):
    def test_robot_with_string(self):
        self.assertEquals("azz", Solution().robotWithString("zza"))

    def test_robot_with_string_1(self):
        self.assertEquals("abc", Solution().robotWithString("bac"))

    def test_robot_with_string_2(self):
        self.assertEquals("addb", Solution().robotWithString("bdda"))

    def test_robot_with_string_3(self):
        self.assertEquals("fnohopzv", Solution().robotWithString("vzhofnpo"))


