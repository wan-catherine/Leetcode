from unittest import TestCase
from problems.N943_Find_The_Shortest_Superstring import Solution

class TestSolution(TestCase):
    def test_shortestSuperstring(self):
        self.assertEqual("leetcodelovesalex", Solution().shortestSuperstring(["alex","loves","leetcode"]))

    def test_shortestSuperstring_1(self):
        self.assertEqual("gctaagttcatgcatc", Solution().shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"]))
