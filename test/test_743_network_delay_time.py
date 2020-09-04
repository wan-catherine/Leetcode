from unittest import TestCase
from problems.N743_Network_Delay_Time import Solution

class TestSolution(TestCase):
    def test_networkDelayTime(self):
        self.assertEqual(2, Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))

    def test_networkDelayTime_1(self):
        self.assertEqual(-1, Solution().networkDelayTime([[1,2,1]], N = 2, K = 2))
