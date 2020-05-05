from unittest import TestCase
from problems.N387_First_Unique_Character_In_String import Solution

class TestSolution(TestCase):
    def test_firstUniqChar(self):
        res = Solution().firstUniqChar("leetcode")
        self.assertEqual(0, res)

    def test_firstUniqChar_1(self):
        res = Solution().firstUniqChar("loveleetcode")
        self.assertEqual(2, res)
