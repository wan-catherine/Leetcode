from unittest import TestCase
from problems.N1562_Find_Latest_Group_Of_Size_M import Solution

class TestSolution(TestCase):
    def test_findLatestStep(self):
        self.assertEqual(4, Solution().findLatestStep(arr = [3,5,1,2,4], m = 1))

    def test_findLatestStep_1(self):
        self.assertEqual(-1, Solution().findLatestStep(arr = [3,1,5,4,2], m = 2))

    def test_findLatestStep_2(self):
        self.assertEqual(1, Solution().findLatestStep(arr = [1], m = 1))

    def test_findLatestStep_3(self):
        self.assertEqual(2, Solution().findLatestStep(arr = [2,1], m = 2))

    def test_findLatestStep_4(self):
        self.assertEqual(-1, Solution().findLatestStep(arr = [3,1,2], m = 2))
