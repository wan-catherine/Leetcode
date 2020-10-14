from unittest import TestCase
from problems.N1319_Number_Of_Operations_To_Make_Network_Connected import Solution

class TestSolution(TestCase):
    def test_makeConnected(self):
        self.assertEqual(1, Solution().makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))

    def test_makeConnected_1(self):
        self.assertEqual(2, Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))

    def test_makeConnected_2(self):
        self.assertEqual(-1, Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))

    def test_makeConnected_3(self):
        self.assertEqual(0, Solution().makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]))
