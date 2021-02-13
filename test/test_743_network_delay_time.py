from unittest import TestCase
from problems.N743_Network_Delay_Time import Solution

class TestSolution(TestCase):
    def test_networkDelayTime(self):
        self.assertEqual(2, Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))

    def test_networkDelayTime_1(self):
        self.assertEqual(-1, Solution().networkDelayTime([[1,2,1]], 2, 2))

    def test_networkDelayTime_2(self):
        self.assertEqual(3, Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1))

    def test_networkDelayTime_3(self):
        self.assertEqual(-1, Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))

