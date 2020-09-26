from unittest import TestCase
from problems.N1405_Longest_Happy_String import Solution

class TestSolution(TestCase):
    def test_longestDiverseString(self):
        self.assertEqual("ccaccbcc", Solution().longestDiverseString(1,1,7))

    def test_longestDiverseString_1(self):
        self.assertEqual("aabbc", Solution().longestDiverseString(2,2,1))

    def test_longestDiverseString_2(self):
        self.assertEqual("aabaa", Solution().longestDiverseString(7,1,0))
