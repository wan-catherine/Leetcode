from unittest import TestCase
from problems.N1463_Cherry_Pickup_II import Solution

class TestSolution(TestCase):
    def test_cherryPickup(self):
        self.assertEqual(24, Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))

    def test_cherryPickup_1(self):
        self.assertEqual(28, Solution().cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))

    def test_cherryPickup_2(self):
        self.assertEqual(22, Solution().cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]))

    def test_cherryPickup_3(self):
        self.assertEqual(4, Solution().cherryPickup([[1,1],[1,1]]))

    def test_cherryPickup_4(self):
        grid = [[0,8,7,10,9,10,0,9,6],[8,7,10,8,7,4,9,6,10],[8,1,1,5,1,5,5,1,2],[9,4,10,8,8,1,9,5,0],[4,3,6,10,9,2,4,8,10],[7,3,2,8,3,3,5,9,8],[1,2,6,5,6,2,0,10,0]]
        self.assertEqual(96, Solution().cherryPickup(grid))
