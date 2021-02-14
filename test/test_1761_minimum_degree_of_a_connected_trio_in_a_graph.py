from unittest import TestCase
from problems.N1761_Minimum_Degree_Of_A_Connected_Trio_In_A_Graph import Solution

class TestSolution(TestCase):
    def test_minTrioDegree(self):
        self.assertEqual(3, Solution().minTrioDegree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]))

    def test_minTrioDegree_1(self):
        self.assertEqual(0, Solution().minTrioDegree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]))
