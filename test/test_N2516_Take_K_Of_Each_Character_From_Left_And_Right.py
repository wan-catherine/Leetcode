from unittest import TestCase
from problems.N2516_Take_K_Of_Each_Character_From_Left_And_Right import Solution

class TestSolution(TestCase):
    def test_take_characters(self):
        self.assertEqual(4, Solution().takeCharacters("ccbabcc", 1))

    def test_take_characters_1(self):
        self.assertEqual(4, Solution().takeCharacters("ccbcac", 1))
