from unittest import TestCase
from problems.N2940_Find_Building_Where_Alice_And_Bob_Can_Meet import Solution

class TestSolution(TestCase):
    def test_leftmost_building_queries(self):
        self.assertListEqual([2,5,-1,5,2], Solution().leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))

    def test_leftmost_building_queries_1(self):
        self.assertListEqual([7,6,-1,4,6], Solution().leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))

    def test_leftmost_building_queries_2(self):
        self.assertListEqual([0,2,2,4,4,2,1,2,3,4,2,2,2,4,4,4,3,4,3,4,4,4,4,4,4], Solution().leftmostBuildingQueries(heights = [3,1,4,2,5], queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]))

    def test_leftmost_building_queries_3(self):
        self.assertListEqual([0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5], Solution().leftmostBuildingQueries(heights = [1,2,1,2,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]))

