from unittest import TestCase
from problems.N3203_Find_Minimum_Diameter_After_Merging_Two_Trees import Solution

class TestSolution(TestCase):
    def test_minimum_diameter_after_merge(self):
        self.assertEquals(3, Solution().minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]))

    def test_minimum_diameter_after_merge_1(self):
        self.assertEquals(5, Solution().minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]))
