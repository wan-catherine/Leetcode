from unittest import TestCase
from problems.N1014_Best_Sightseeing_Pair import Solution

class TestSolution(TestCase):
    def test_maxScoreSightseeingPair(self):
        self.assertEqual(11, Solution().maxScoreSightseeingPair([8,1,5,2,6]))
