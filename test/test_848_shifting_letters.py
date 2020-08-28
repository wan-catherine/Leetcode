from unittest import TestCase
from problems.N848_Shifting_Letters import Solution

class TestSolution(TestCase):
    def test_shiftingLetters(self):
        self.assertEqual("rpl", Solution().shiftingLetters(S = "abc", shifts = [3,5,9]))
