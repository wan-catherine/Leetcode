from unittest import TestCase
from problems.SubstringConcatenationAllWords import Solution

class TestSolution(TestCase):
    def test_findSubstring(self):
        solution = Solution()
        res = solution.findSubstring("barfoothefoobarman", ["foo","bar"])
        self.assertEqual([0,9], res)

    def test_findSubstring_six(self):
        solution = Solution()
        res = solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
        self.assertEqual([6,9,12], res)

    def test_findSubstring_zero(self):
        solution = Solution()
        res = solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
        self.assertEqual([8], res)

    def test_findSubstring_empty(self):
        solution = Solution()
        res = solution.findSubstring("wordgoodstudentgoodword", ["word","student"])
        self.assertEqual([], res)

    def test_findSubstring_empty_empty(self):
        solution = Solution()
        res = solution.findSubstring("", [])
        self.assertEqual([], res)