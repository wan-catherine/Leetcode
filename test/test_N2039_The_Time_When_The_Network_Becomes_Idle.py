from unittest import TestCase
from problems.N2039_The_Time_When_The_Network_Becomes_Idle import Solution

class TestSolution(TestCase):
    def test_network_becomes_idle(self):
        self.assertEqual(8, Solution().networkBecomesIdle(edges = [[0,1],[1,2]], patience = [0,2,1]))

    def test_network_becomes_idle_1(self):
        self.assertEqual(3, Solution().networkBecomesIdle(edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]))