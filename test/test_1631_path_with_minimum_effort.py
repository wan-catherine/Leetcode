from unittest import TestCase
from problems.N1631_Path_With_Minimum_Effort import Solution

class TestSolution(TestCase):
    def test_minimumEffortPath(self):
        self.assertEqual(2, Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))

    def test_minimumEffortPath_1(self):
        self.assertEqual(1, Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))

    def test_minimumEffortPath_2(self):
        self.assertEqual(0, Solution().minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))

    def test_minimumEffortPath_3(self):
        self.assertEqual(0, Solution().minimumEffortPath([[3]]))