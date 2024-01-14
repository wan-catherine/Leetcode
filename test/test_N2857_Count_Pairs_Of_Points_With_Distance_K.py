from unittest import TestCase
from problems.N2857_Count_Pairs_Of_Points_With_Distance_K import Solution

class TestSolution(TestCase):
    def test_count_pairs(self):
        self.assertEqual(2, Solution().countPairs(coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5))

    def test_count_pairs_1(self):
        self.assertEqual(10, Solution().countPairs(coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0))
