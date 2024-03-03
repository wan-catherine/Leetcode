from unittest import TestCase
from problems.N3067_Count_Pairs_Of_Connectable_Servers_In_A_Weighted_Tree_Network import Solution

class TestSolution(TestCase):
    def test_count_pairs_of_connectable_servers(self):
        self.assertListEqual([0,4,6,6,4,0], Solution().countPairsOfConnectableServers(edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1))

    def test_count_pairs_of_connectable_servers_1(self):
        self.assertListEqual([2,0,0,0,0,0,2], Solution().countPairsOfConnectableServers(edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3))
