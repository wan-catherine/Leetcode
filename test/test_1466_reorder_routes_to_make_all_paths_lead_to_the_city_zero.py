from unittest import TestCase
from problems.N1466_Reorder_Routes_To_Make_All_Paths_Lead_To_The_City_Zero import Solution

class TestSolution(TestCase):
    def test_minReorder(self):
        self.assertEqual(3, Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))

    def test_minReorder_1(self):
        self.assertEqual(2, Solution().minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))

    def test_minReorder_2(self):
        self.assertEqual(0, Solution().minReorder(n = 3, connections = [[1,0],[2,0]]))

    def test_minReorder_3(self):
        self.assertEqual(0, Solution().minReorder(n = 3, connections = [[1,2],[2,0]]))
