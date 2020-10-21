from unittest import TestCase
from problems.N820_Short_Encoding_Of_Words import Solution

class TestSolution(TestCase):
    def test_minimumLengthEncoding(self):
        self.assertEqual(10, Solution().minimumLengthEncoding(["time", "me", "bell"]))
