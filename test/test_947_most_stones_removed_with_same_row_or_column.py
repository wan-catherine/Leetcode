from unittest import TestCase
from problems.N947_Most_Stones_Removed_With_Same_Row_Or_Column import Solution

class TestSolution(TestCase):
    def test_removeStones(self):
        self.assertEqual(5, Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))

    def test_removeStones_1(self):
        self.assertEqual(3, Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))

    def test_removeStones_2(self):
        self.assertEqual(0, Solution().removeStones([[0,0]]))

    def test_removeStones_3(self):
        self.assertEqual(4, Solution().removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))

    def test_removeStones_4(self):
        self.assertEqual(8, Solution().removeStones([[4,4],[5,5],[3,1],[1,4],[1,1],[2,3],[0,3],[2,4],[3,5]]))
