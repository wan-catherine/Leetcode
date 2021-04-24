from unittest import TestCase
from problems.N1192_Critical_Connections_In_A_Network import Solution

class TestSolution(TestCase):
    def test_critical_connections(self):
        self.assertListEqual([[1,3]], Solution().criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
