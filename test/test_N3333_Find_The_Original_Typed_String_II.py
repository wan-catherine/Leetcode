from unittest import TestCase
from problems.N3333_Find_The_Original_Typed_String_II import Solution

class TestSolution(TestCase):
    def test_possible_string_count(self):
        self.assertEquals(5, Solution().possibleStringCount(word = "aabbccdd", k = 7))

    def test_possible_string_count_1(self):
        self.assertEquals(1, Solution().possibleStringCount(word = "aabbccdd", k = 8))

    def test_possible_string_count_2(self):
        self.assertEquals(8, Solution().possibleStringCount(word = "aaabbb", k = 3))
