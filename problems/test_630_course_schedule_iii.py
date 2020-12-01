from unittest import TestCase
from problems.N630_Course_Schedule_III import Solution

class TestSolution(TestCase):
    def test_scheduleCourse(self):
        self.assertEqual(3, Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))

    def test_scheduleCourse_1(self):
        self.assertEqual(2, Solution().scheduleCourse([[5,5],[4,6],[2,6]]))

    def test_scheduleCourse_2(self):
        self.assertEqual(1, Solution().scheduleCourse([[100,2],[32,50]]))
