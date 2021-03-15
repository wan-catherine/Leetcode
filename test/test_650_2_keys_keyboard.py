from unittest import TestCase
from problems.N650_2_Keys_Keyboard import Solution

class TestSolution(TestCase):
    def test_minSteps(self):
        self.assertEqual(3, Solution().minSteps(3))

    def test_minSteps_1(self):
        self.assertEqual(2, Solution().minSteps(2))