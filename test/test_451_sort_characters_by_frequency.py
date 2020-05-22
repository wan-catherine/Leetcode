from unittest import TestCase
from problems.N451_Sort_Characters_By_Frequency import Solution

class TestSolution(TestCase):
    def test_frequencySort(self):
        self.assertEqual("eetr", Solution().frequencySort("tree"))

    def test_frequencySort_1(self):
        self.assertEqual("cccaaa", Solution().frequencySort("cccaaa"))