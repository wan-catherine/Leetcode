from unittest import TestCase
from problems.N1621_Number_Of_Sets_Of_K_Non_Overlapping_Line_Segments import Solution

class TestSolution(TestCase):
    def test_numberOfSets(self):
        self.assertEqual(5, Solution().numberOfSets(4, 2))

    def test_numberOfSets_1(self):
        self.assertEqual(3, Solution().numberOfSets(3, 1))

    def test_numberOfSets_2(self):
        self.assertEqual(796297179, Solution().numberOfSets(30, 7))

    def test_numberOfSets_3(self):
        self.assertEqual(7, Solution().numberOfSets(5, 3))

    def test_numberOfSets_4(self):
        self.assertEqual(1, Solution().numberOfSets(3, 2))


