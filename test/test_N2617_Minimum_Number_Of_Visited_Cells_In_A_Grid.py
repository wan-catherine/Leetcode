from unittest import TestCase
from problems.N2617_Minimum_Number_Of_Visited_Cells_In_A_Grid import Solution

class TestSolution(TestCase):
    def test_minimum_visited_cells(self):
        self.assertEqual(4, Solution().minimumVisitedCells([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))

    def test_minimum_visited_cells_1(self):
        self.assertEqual(3, Solution().minimumVisitedCells([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))

    def test_minimum_visited_cells_2(self):
        self.assertEqual(-1, Solution().minimumVisitedCells([[2,1,0],[1,0,0]]))

    def test_minimum_visited_cells_3(self):
        self.assertEqual(3, Solution().minimumVisitedCells([[6,4,8],[7,3,2],[2,1,11],[8,13,12],[4,3,0]]))

    def test_minimum_visited_cells_4(self):
        self.assertEqual(3, Solution().minimumVisitedCells([[12,6,18,21,18],[17,17,22,0,2],[16,8,22,12,11],[4,15,15,21,6],[0,5,0,6,0]]))

