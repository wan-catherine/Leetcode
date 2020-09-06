from unittest import TestCase
from problems.N1297_Maximum_Number_Of_Occurrences_Of_A_Substring import Solution

class TestSolution(TestCase):
    def test_maxFreq(self):
        self.assertEqual(2, Solution().maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))

    def test_maxFreq_1(self):
        self.assertEqual(2, Solution().maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))

    def test_maxFreq_2(self):
        self.assertEqual(3, Solution().maxFreq(s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3))

    def test_maxFreq_3(self):
        self.assertEqual(0, Solution().maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3))

    # def test_maxFreq(self):
    #     self.assertEqual(2, Solution().maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
