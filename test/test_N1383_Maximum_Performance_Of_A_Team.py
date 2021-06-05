from unittest import TestCase
from problems.N1383_Maximum_Performance_Of_A_Team import Solution

class TestSolution(TestCase):
    def test_max_performance(self):
        self.assertEqual(60, Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))

    def test_max_performance_1(self):
        self.assertEqual(68, Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3))

    def test_max_performance_2(self):
        self.assertEqual(72, Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4))

    def test_max_performance_3(self):
        self.assertEqual(56, Solution().maxPerformance(3, [2,8,2], [2,7,1], 2))
