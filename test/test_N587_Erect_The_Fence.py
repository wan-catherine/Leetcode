from unittest import TestCase
from problems.N587_Erect_The_Fence import Solution

class TestSolution(TestCase):
    def test_outer_trees(self):
        self.assertListEqual([[1,1],[2,0],[3,3],[2,4],[4,2]], Solution().outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))

    def test_outer_trees_1(self):
        self.assertListEqual([[4,2],[2,2],[1,2]], Solution().outerTrees([[1,2],[2,2],[4,2]]))
