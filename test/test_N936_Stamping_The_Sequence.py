from unittest import TestCase
from problems.N936_Stamping_The_Sequence import Solution

class TestSolution(TestCase):
    def test_moves_to_stamp(self):
        self.assertListEqual([0,2], Solution().movesToStamp(stamp = "abc", target = "ababc"))

    def test_moves_to_stamp_1(self):
        self.assertListEqual([3,0,1], Solution().movesToStamp(stamp = "abca", target = "aabcaca"))
