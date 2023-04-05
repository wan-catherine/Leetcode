from unittest import TestCase
from problems.N2514_Count_Anagrams import Solution

class TestSolution(TestCase):
    def test_count_anagrams(self):
        self.assertEqual(18, Solution().countAnagrams("too hot"))

    def test_count_anagrams_1(self):
        self.assertEqual(1, Solution().countAnagrams("aa"))

    def test_count_anagrams_2(self):
        self.assertEqual(2520, Solution().countAnagrams("ptx cccbhbq"))
