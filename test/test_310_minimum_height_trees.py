from unittest import TestCase
from problems.N310_Minimum_Height_Trees import Solution

class TestSolution(TestCase):
    def test_findMinHeightTrees(self):
        self.assertListEqual([1], Solution().findMinHeightTrees(n = 4, edges = [[1, 0], [1, 2], [1, 3]]))

    def test_findMinHeightTrees_1(self):
        self.assertListEqual([3,4], Solution().findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))

    def test_findMinHeightTrees_2(self):
        self.assertListEqual([0], Solution().findMinHeightTrees(n = 1, edges = []))

    def test_findMinHeightTrees_3(self):
        self.assertListEqual([1,2], Solution().findMinHeightTrees(n = 7, edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]))
