from unittest import TestCase
from problems.CourseScheduleII import Solution

class TestSolution(TestCase):
    def test_findOrder(self):
        solution = Solution()
        res = solution.findOrder(2, [[1,0]] )
        self.assertEqual(res, [0,1])

    def test_findOrder_one(self):
        solution = Solution()
        res = solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
        self.assertEqual(res, [0,1,2,3] )

    def test_findOrder_two(self):
        solution = Solution()
        res = solution.findOrder(2, [[0,1],[1,0]] )
        self.assertEqual(res, [])