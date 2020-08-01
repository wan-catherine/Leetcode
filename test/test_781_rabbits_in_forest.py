from unittest import TestCase
from problems.N781_Rabbits_In_Forest import Solution

class TestSolution(TestCase):
    def test_numRabbits(self):
        answers = [1, 1, 2]
        self.assertEqual(5, Solution().numRabbits(answers))

    def test_numRabbits_1(self):
        answers = [10, 10, 10]
        self.assertEqual(11, Solution().numRabbits(answers))

    def test_numRabbits_2(self):
        answers = []
        self.assertEqual(0, Solution().numRabbits(answers))
