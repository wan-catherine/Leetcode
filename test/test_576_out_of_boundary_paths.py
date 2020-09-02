from unittest import TestCase
from problems.N576_Out_Of_Boundary_Paths import Solution

class TestSolution(TestCase):
    def test_findPaths(self):
        self.assertEqual(6, Solution().findPaths(2,2,2,0,0))

    def test_findPaths_1(self):
        self.assertEqual(12, Solution().findPaths(1,3,3,0,1))

    def test_findPaths_2(self):
        self.assertEqual(0, Solution().findPaths(3,8,0,2,0))

    def test_findPaths_3(self):
        self.assertEqual(102984580, Solution().findPaths(8,7,16,1,5))
