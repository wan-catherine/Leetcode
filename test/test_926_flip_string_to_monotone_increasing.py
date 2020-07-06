from unittest import TestCase
from problems.N926_Flip_String_To_Monotone_Increasing import Solution

class TestSolution(TestCase):
    def test_minFlipsMonoIncr(self):
        self.assertEqual(1, Solution().minFlipsMonoIncr("00110"))

    def test_minFlipsMonoIncr_1(self):
        self.assertEqual(2, Solution().minFlipsMonoIncr("010110"))

    def test_minFlipsMonoIncr_2(self):
        self.assertEqual(2, Solution().minFlipsMonoIncr("00011000"))

    def test_minFlipsMonoIncr_3(self):
        self.assertEqual(3, Solution().minFlipsMonoIncr("0101100011"))


