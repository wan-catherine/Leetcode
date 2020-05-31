from unittest import TestCase
from problems.N739_Daily_Temperatures import Solution

class TestSolution(TestCase):
    def test_dailyTemperatures(self):
        self.assertListEqual([1, 1, 4, 2, 1, 1, 0, 0], Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

    def test_dailyTemperatures_1(self):
        self.assertListEqual([3,1,1,2,1,1,0,1,1,0], Solution().dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))
