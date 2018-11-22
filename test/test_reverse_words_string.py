from unittest import TestCase
from problems.ReverseWordsString import Solution

class TestSolution(TestCase):
    def test_reverseWords(self):
        solution = Solution()
        res = solution.reverseWords("the sky is blue")
        self.assertEqual("blue is sky the", res)
