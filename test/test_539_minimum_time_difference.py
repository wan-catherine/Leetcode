from unittest import TestCase
from problems.N539_Minimum_Time_Difference import Solution

class TestSolution(TestCase):
    def test_findMinDifference(self):
        self.assertEqual(1, Solution().findMinDifference(["23:59","00:00"]))

    def test_findMinDifference_1(self):
        self.assertEqual(147, Solution().findMinDifference(["05:31","22:08","00:35"]))
