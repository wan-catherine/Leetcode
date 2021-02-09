from unittest import TestCase
from problems.N1751_Maximum_Number_Of_Events_That_Can_Be_Attended_II import Solution

class TestSolution(TestCase):
    def test_maxValue(self):
        self.assertEqual(7, Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2))

    def test_maxValue_1(self):
        self.assertEqual(10, Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2))

    def test_maxValue_2(self):
        self.assertEqual(9, Solution().maxValue(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3))
