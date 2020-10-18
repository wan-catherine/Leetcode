from unittest import TestCase
from problems.N1627_Graph_Connectivity_With_Threshold import Solution
false = False
true = True

class TestSolution(TestCase):
    def test_areConnected(self):
        self.assertListEqual([false,false,true], Solution().areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]))

    def test_areConnected_1(self):
        self.assertListEqual([true,true,true,true,true], Solution().areConnected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]))

    def test_areConnected_2(self):
        self.assertListEqual([false,false,false,false,false], Solution().areConnected(n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]))
