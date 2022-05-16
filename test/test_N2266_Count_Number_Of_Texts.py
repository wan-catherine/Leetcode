from unittest import TestCase
from problems.N2266_Count_Number_Of_Texts import Solution

class TestSolution(TestCase):
    def test_count_texts(self):
        self.assertEqual(8, Solution().countTexts("22233"))

    def test_count_texts_1(self):
        self.assertEqual(82876089, Solution().countTexts("222222222222222222222222222222222222"))