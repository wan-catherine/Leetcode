from unittest import TestCase
from problems.N2156_Find_Substring_With_Given_Hash_Value import Solution

class TestSolution(TestCase):
    def test_sub_str_hash(self):
        self.assertEqual("ee", Solution().subStrHash(s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0))

    def test_sub_str_hash_1(self):
        self.assertEqual("fbx", Solution().subStrHash(s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32))
