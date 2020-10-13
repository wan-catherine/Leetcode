from unittest import TestCase
from problems.N1129_Shortest_Path_With_Alternating_Colors import Solution

class TestSolution(TestCase):
    def test_shortestAlternatingPaths(self):
        self.assertListEqual([0,1,-1], Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[1,2]], blue_edges = []))

    def test_shortestAlternatingPaths_1(self):
        self.assertListEqual([0,1,-1], Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]))

    def test_shortestAlternatingPaths_2(self):
        self.assertListEqual([0,-1,-1], Solution().shortestAlternatingPaths(n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]))

    def test_shortestAlternatingPaths_3(self):
        self.assertListEqual([0,1,2], Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]))

    def test_shortestAlternatingPaths_4(self):
        self.assertListEqual([0,1,1], Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]))

    def test_shortestAlternatingPaths_5(self):
        self.assertListEqual([0,1,2,3,7], Solution().shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))

    def test_shortestAlternatingPaths_6(self):
        self.assertListEqual([0,2,-1,-1,1], Solution().shortestAlternatingPaths(5, [[3,2],[4,1],[1,4],[2,4]], [[2,3],[0,4],[4,3],[4,4],[4,0],[1,0]]))

    def test_shortestAlternatingPaths_7(self):
        self.assertListEqual([0,1,2,1,1], Solution().shortestAlternatingPaths(5, [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]], [[1,3],[0,0],[0,3],[4,2],[1,0]]))