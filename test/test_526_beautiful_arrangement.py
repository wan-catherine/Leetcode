from unittest import TestCase
from problems.N526_Beautiful_Arrangement import Solution

class TestSolution(TestCase):
    def test_countArrangement(self):
        self.assertEqual(2, Solution().countArrangement(2))

    def test_countArrangement_1(self):
        self.assertEqual(1, Solution().countArrangement(1))

    def test_countArrangement_2(self):
        self.assertEqual(3, Solution().countArrangement(3))

    def test_countArrangement_4(self):
        self.assertEqual(8, Solution().countArrangement(4))