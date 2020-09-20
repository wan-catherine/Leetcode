from unittest import TestCase
from problems.N980_Unique_Paths_III import Solution

class TestSolution(TestCase):
    def test_uniquePathsIII(self):
        self.assertEqual(2, Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))

    def test_uniquePathsIII_1(self):
        self.assertEqual(4, Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))

    def test_uniquePathsIII_2(self):
        self.assertEqual(0, Solution().uniquePathsIII([[0,1],[2,0]]))