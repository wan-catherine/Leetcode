from unittest import TestCase
from problems.N1267_Count_Servers_That_Communicate import Solution

class TestSolution(TestCase):
    def test_countServers(self):
        grid = [[1,0],[0,1]]
        self.assertEqual(0, Solution().countServers(grid))

    def test_countServers_1(self):
        grid = [[1,0],[1,1]]
        self.assertEqual(3, Solution().countServers(grid))

    def test_countServers_2(self):
        grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
        self.assertEqual(4, Solution().countServers(grid))
