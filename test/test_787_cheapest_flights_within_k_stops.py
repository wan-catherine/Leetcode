from unittest import TestCase
from problems.N787_Cheapest_Flights_Within_K_Stops import Solution

class TestSolution(TestCase):
    def test_findCheapestPrice(self):
        n = 3
        edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(200, Solution().findCheapestPrice(n, edges, src,dst,k))

    def test_findCheapestPrice_1(self):
        n = 3
        edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(500, Solution().findCheapestPrice(n, edges, src,dst,k))

    def test_findCheapestPrice_2(self):
        n = 10
        edges = [[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10], [6, 8, 6], [7, 9, 4], [1, 5, 4], [1, 0, 4],
         [9, 7, 3], [7, 0, 5], [6, 5, 8], [1, 7, 6], [4, 0, 9], [5, 9, 1], [8, 7, 3], [1, 2, 6], [4, 1, 5], [5, 2, 4],
         [1, 9, 1], [7, 8, 10], [0, 4, 2], [7, 2, 8]]
        src = 6
        dst = 0
        k = 7
        self.assertEqual(14, Solution().findCheapestPrice(n, edges, src,dst,k))

    def test_findCheapestPrice_3(self):
        n = 4
        edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(6, Solution().findCheapestPrice(n, edges, src,dst,k))
