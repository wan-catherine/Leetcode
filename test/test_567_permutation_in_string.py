from unittest import TestCase
from problems.N567_Permutation_In_String import Solution

class TestSolution(TestCase):
    def test_checkInclusion(self):
        self.assertEqual(True, Solution().checkInclusion("ab", "eidbaooo"))

    def test_checkInclusion_1(self):
        self.assertEqual(False, Solution().checkInclusion("ab", "eidboaoo"))

    def test_checkInclusion_2(self):
        self.assertEqual(False, Solution().checkInclusion("hello", "ooolleoooleh"))

    def test_checkInclusion_3(self):
        self.assertEqual(True, Solution().checkInclusion("adc", "dcda"))

    def test_checkInclusion_4(self):
        self.assertEqual(False, Solution().checkInclusion("mart", "karma"))

    def test_checkInclusion_5(self):
        self.assertEqual(True, Solution().checkInclusion("r", "pilmtnzraxj"))

    def test_checkInclusion_6(self):
        self.assertEqual(False, Solution().checkInclusion("qff", "ifisnoskikfqzrmzlv"))
