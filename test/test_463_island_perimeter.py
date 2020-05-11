from unittest import TestCase
from problems.N463_Island_Perimeter import Solution

class TestSolution(TestCase):
    def test_islandPerimeter(self):
        self.assertEqual(16, Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
