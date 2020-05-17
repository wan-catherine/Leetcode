from unittest import TestCase
from problems.N438_Find_All_Anagrams_In_A_String import Solution

class TestSolution(TestCase):
    def test_findAnagrams(self):
        self.assertListEqual([0,6], Solution().findAnagrams("cbaebabacd", "abc"))

    def test_findAnagrams_1(self):
        self.assertListEqual([0,1,2], Solution().findAnagrams("abab", "ab"))


