from unittest import TestCase
from problems.N1739_Building_Boxes import Solution

class TestSolution(TestCase):
    def test_minimumBoxes(self):
        self.assertEqual(3, Solution().minimumBoxes(3))

    def test_minimumBoxes_1(self):
        self.assertEqual(3, Solution().minimumBoxes(4))

    def test_minimumBoxes_2(self):
        self.assertEqual(6, Solution().minimumBoxes(10))

    def test_minimumBoxes_3(self):
        self.assertEqual(9, Solution().minimumBoxes(15))
