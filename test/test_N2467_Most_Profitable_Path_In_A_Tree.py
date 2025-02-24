from unittest import TestCase
from problems.N2467_Most_Profitable_Path_In_A_Tree import Solution

class TestSolution(TestCase):
    def test_most_profitable_path(self):
        self.assertEquals(6, Solution().mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]))

    def test_most_profitable_path_1(self):
        self.assertEquals(-7280, Solution().mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350]))
