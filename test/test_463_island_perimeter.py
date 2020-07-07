from unittest import TestCase
from problems.N463_Island_Perimeter import Solution

class TestSolution(TestCase):
    def test_islandPerimeter(self):
        self.assertEqual(16, Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))

    def test_islandPerimeter_1(self):
        self.assertEqual(4, Solution().islandPerimeter([[0],[1]]))

    def test_islandPerimeter_2(self):
        self.assertEqual(8, Solution().islandPerimeter([[1,1],[1,1]]))
