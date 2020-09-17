from unittest import TestCase
from problems.N808_Soup_Servings import Solution

class TestSolution(TestCase):
    def test_soupServings(self):
        self.assertEqual(0.625, Solution().soupServings(50))
