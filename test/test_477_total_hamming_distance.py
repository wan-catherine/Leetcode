from unittest import TestCase
from problems.N477_Total_Hamming_Distance import Solution

class TestSolution(TestCase):
    def test_totalHammingDistance(self):
        self.assertEqual(6, Solution().totalHammingDistance([4, 14, 2]))

    def test_totalHammingDistance_1(self):
        self.assertEqual(22, Solution().totalHammingDistance([6,1,8,6,8]))