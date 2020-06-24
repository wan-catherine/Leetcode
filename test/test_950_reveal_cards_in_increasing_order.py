from unittest import TestCase
from problems.N950_Reveal_Cards_In_Increasing_Order import Solution

class TestSolution(TestCase):
    def test_deckRevealedIncreasing(self):
        input = [17,13,11,2,3,5,7]
        output = [2,13,3,11,5,17,7]
        self.assertListEqual(output, Solution().deckRevealedIncreasing(input))
