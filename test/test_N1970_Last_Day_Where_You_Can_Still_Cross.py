from unittest import TestCase
from problems.N1970_Last_Day_Where_You_Can_Still_Cross import Solution

class TestSolution(TestCase):
    def test_latest_day_to_cross(self):
        self.assertEqual(2, Solution().latestDayToCross(row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]))

    def test_latest_day_to_cross_1(self):
        self.assertEqual(1, Solution().latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]))

    def test_latest_day_to_cross_2(self):
        self.assertEqual(3, Solution().latestDayToCross(row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))

    def test_latest_day_to_cross_3(self):
        self.assertEqual(3, Solution().latestDayToCross(6, 2, [[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]]))