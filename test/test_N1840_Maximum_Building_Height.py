from unittest import TestCase
from problems.N1840_Maximum_Building_Height import Solution

class TestSolution(TestCase):
    def test_max_building(self):
        self.assertEqual(2, Solution().maxBuilding(n = 5, restrictions = [[2,1],[4,1]]))

    def test_max_building_1(self):
        self.assertEqual(5, Solution().maxBuilding(n = 6, restrictions = []))

    def test_max_building_2(self):
        self.assertEqual(5, Solution().maxBuilding(n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]))

    def test_max_building_3(self):
        self.assertEqual(2, Solution().maxBuilding(10, [[6,2],[5,1],[2,4],[3,0],[9,5],[7,0],[4,2],[10,3],[8,0]]))
