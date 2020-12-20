from unittest import TestCase
from problems.N741_Cherry_Pickup import Solution

class TestSolution(TestCase):
    def test_cherryPickup(self):
        self.assertEqual(5, Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))

    def test_cherryPickup_1(self):
        self.assertEqual(0, Solution().cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]))
