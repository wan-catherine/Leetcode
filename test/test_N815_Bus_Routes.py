from unittest import TestCase
from problems.N815_Bus_Routes import Solution

class TestSolution(TestCase):
    def test_num_buses_to_destination(self):
        self.assertEqual(2, Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))

    def test_num_buses_to_destination_1(self):
        self.assertEqual(-1, Solution().numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))

    def test_num_buses_to_destination_2(self):
        self.assertEqual(-1, Solution().numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]], 7, 47))

    def test_num_buses_to_destination_3(self):
        self.assertEqual(0, Solution().numBusesToDestination([[1,7],[3,5]], 5, 5))