from unittest import TestCase
from problems.CourseSchedule import Solution

class TestSolution(TestCase):
    def test_canFinish(self):
        solution = Solution()
        res = solution.canFinish(2, [[1,0]] )
        self.assertEqual(True, res)

    def test_canFinish_one(self):
        solution = Solution()
        res = solution.canFinish(2, [[1,0],[0,1]])
        self.assertEqual(False, res)

    def test_canFinish_two(self):
        solution = Solution()
        res = solution.canFinish(1, [])
        self.assertEqual(True, res)

    def test_canFinish_three(self):
        solution = Solution()
        res = solution.canFinish(3, [[1,0]])
        self.assertEqual(True, res)

    def test_canFinish_four(self):
        solution = Solution()
        res = solution.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
        self.assertEqual(True, res)

    def test_canFinish_1(self):
        solution = Solution()
        res = solution.canFinish(3,[[1,0],[0,2],[2,1]])
        self.assertEqual(False, res)

    def test_canFinish_2(self):
        solution = Solution()
        res = solution.canFinish(4,[[0,1],[3,1],[1,3],[3,2]])
        self.assertEqual(False, res)

    def test_canFinish_3(self):
        solution = Solution()
        res = solution.canFinish(4, [[1,0],[2,0],[3,1],[3,2]])
        self.assertEqual(True, res)