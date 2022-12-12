from unittest import TestCase
from problems.N2503_Maximum_Number_Of_Points_From_Grid_Queries import Solution

class TestSolution(TestCase):
    def test_max_points(self):
        self.assertListEqual([5,8,1], Solution().maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
