from unittest import TestCase
from problems.N1579_Remove_Max_Number_Of_Edges_To_Keep_Graph_Fully_Traversable import Solution

class TestSolution(TestCase):
    def test_maxNumEdgesToRemove(self):
        self.assertEqual(2, Solution().maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))

    def test_maxNumEdgesToRemove_1(self):
        self.assertEqual(0, Solution().maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))

    def test_maxNumEdgesToRemove_2(self):
        self.assertEqual(-1, Solution().maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))

    def test_maxNumEdgesToRemove_3(self):
        self.assertEqual(9, Solution().maxNumEdgesToRemove(n = 19, edges = [[1,1,2],[2,1,2],[1,2,3],[2,2,3],[1,1,4],[2,1,4],[1,1,5],[2,1,5],[3,4,6],[3,3,7],[1,2,8],[2,2,8],[3,1,9],[1,3,10],[2,3,10],[1,8,11],[2,8,11],[1,5,12],[2,5,12],[1,8,13],[2,8,13],[3,10,14],[1,9,15],[2,9,15],[3,13,16],[3,9,17],[3,11,18],[1,1,19],[2,1,19],[2,4,10],[2,2,4],[2,3,18],[2,14,15],[1,4,17],[1,7,10],[1,6,14],[1,3,12],[1,5,14]]))
