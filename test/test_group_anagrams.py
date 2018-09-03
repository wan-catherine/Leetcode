from unittest import TestCase
from problems.GroupAnagrams import Solution

class TestSolution(TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        res = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        l = [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
        self.assertTrue(l[2] in res)