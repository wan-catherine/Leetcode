from unittest import TestCase
from problems.N1368_Minimum_Cost_To_Make_At_Least_One_Valid_Path_In_A_Grid import Solution

class TestSolution(TestCase):
    def test_min_cost(self):
        self.assertEqual(3, Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))

    def test_min_cost_1(self):
        self.assertEqual(0, Solution().minCost([[1,1,3],[3,2,2],[1,1,4]]))

    def test_min_cost_2(self):
        self.assertEqual(1, Solution().minCost([[1,2],[4,3]]))

