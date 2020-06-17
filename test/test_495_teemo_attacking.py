from unittest import TestCase
from problems.N495_Teemo_Attacking import Solution

class TestSolution(TestCase):
    def test_findPoisonedDuration(self):
        self.assertEqual(4, Solution().findPoisonedDuration([1,4], 2))

    def test_findPoisonedDuration_1(self):
        self.assertEqual(3, Solution().findPoisonedDuration([1,2], 2))
