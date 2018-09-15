from unittest import TestCase
from problems.LengthLastWord import Solution

class TestSolution(TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        res = solution.lengthOfLastWord("Hello World")
        self.assertTrue(5, res)
