from unittest import TestCase
from problems.N1391_Check_If_There_Is_A_Valid_Path_In_A_Grid import Solution

class TestSolution(TestCase):
    def test_hasValidPath(self):
        self.assertTrue(Solution().hasValidPath(grid = [[2,4,3],[6,5,2]]))

    def test_hasValidPath_1(self):
        self.assertFalse(Solution().hasValidPath(grid = [[1,2,1],[1,2,1]]))

    def test_hasValidPath_2(self):
        self.assertFalse(Solution().hasValidPath(grid = [[1,1,2]]))

    def test_hasValidPath_3(self):
        self.assertTrue(Solution().hasValidPath(grid = [[1,1,1,1,1,1,3]]))

    def test_hasValidPath_4(self):
        self.assertTrue(Solution().hasValidPath(grid = [[2],[2],[2],[2],[2],[2],[6]]))
