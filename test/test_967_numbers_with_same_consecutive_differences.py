from unittest import TestCase
from problems.N967_Numbers_With_Same_Consecutive_Differences import Solution

class TestSolution(TestCase):
    def test_numsSameConsecDiff(self):
        self.assertSetEqual(set([181,292,707,818,929]), set(Solution().numsSameConsecDiff(3, 7)))

    def test_numsSameConsecDiff_1(self):
        self.assertSetEqual(set([10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]), set(Solution().numsSameConsecDiff(2, 1)))

    def test_numsSameConsecDiff_2(self):
        self.assertSetEqual(set([11,22,33,44,55,66,77,88,99]), set(Solution().numsSameConsecDiff(2, 0)))
