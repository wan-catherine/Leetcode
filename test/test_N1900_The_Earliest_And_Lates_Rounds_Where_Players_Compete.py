from unittest import TestCase
from problems.N1900_The_Earliest_And_Lates_Rounds_Where_Players_Compete import Solution

class TestSolution(TestCase):
    def test_earliest_and_latest(self):
        self.assertListEqual([3,4], Solution().earliestAndLatest(n = 11, firstPlayer = 2, secondPlayer = 4))

    def test_earliest_and_latest_1(self):
        self.assertListEqual([1,1], Solution().earliestAndLatest(n = 5, firstPlayer = 1, secondPlayer = 5))

    def test_earliest_and_latest_2(self):
        self.assertListEqual([2,3], Solution().earliestAndLatest(n = 10, firstPlayer = 1, secondPlayer = 8))
