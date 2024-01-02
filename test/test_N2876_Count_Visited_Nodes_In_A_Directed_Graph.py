from unittest import TestCase
from problems.N2876_Count_Visited_Nodes_In_A_Directed_Graph import Solution

class TestSolution(TestCase):
    def test_count_visited_nodes(self):
        self.assertListEqual([3,3,3,4], Solution().countVisitedNodes([1,2,0,0]))

    def test_count_visited_nodes_1(self):
        self.assertListEqual([5,5,5,5,5], Solution().countVisitedNodes([1,2,3,4,0]))

    def test_count_visited_nodes_2(self):
        self.assertListEqual([2,7,8,2,5,4,6,3], Solution().countVisitedNodes([3,6,1,0,5,7,4,3]))

