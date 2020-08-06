from unittest import TestCase
from problems.N1138_Alphabet_Board_Path import Solution

class TestSolution(TestCase):
    def test_alphabetBoardPath(self):
        self.assertEqual("DDR!UURRR!!DDD!", Solution().alphabetBoardPath("leet"))

    def test_alphabetBoardPath_1(self):
        self.assertEqual("RR!DDRR!UUL!R!", Solution().alphabetBoardPath("code"))

    def test_alphabetBoardPath_2(self):
        self.assertEqual("DDDDD!UUUUURRR!DDDDLLLD!", Solution().alphabetBoardPath("zdz"))