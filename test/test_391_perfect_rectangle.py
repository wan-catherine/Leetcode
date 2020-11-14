from unittest import TestCase
from problems.N391_Perfect_Rectangle import Solution

class TestSolution(TestCase):
    def test_isRectangleCover(self):
        self.assertTrue(Solution().isRectangleCover( [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]))

    def test_isRectangleCover_1(self):
        self.assertFalse(Solution().isRectangleCover( [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]))

    def test_isRectangleCover_2(self):
        self.assertFalse(Solution().isRectangleCover( [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]))

    def test_isRectangleCover_3(self):
        self.assertFalse(Solution().isRectangleCover( [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]))

    def test_isRectangleCover_4(self):
        self.assertFalse(Solution().isRectangleCover([[0,0,1,1],[0,1,1,2],[0,2,1,3],[1,0,2,1],[1,0,2,1],[1,2,2,3],[2,0,3,1],[2,1,3,2],[2,2,3,3]]))

    def test_isRectangleCover_5(self):
        self.assertTrue(Solution().isRectangleCover([[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]))