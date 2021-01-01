from unittest import TestCase
from problems.N666_Path_Sum_IV import Solution

class TestSolution(TestCase):
    def test_pathSum(self):
        self.assertEqual(12, Solution().pathSum([113, 215, 221]))

    def test_pathSum_1(self):
        self.assertEqual(4, Solution().pathSum([113, 221]))

    def test_pathSum_2(self):
        self.assertEqual(20, Solution().pathSum([111,217,221,315,415]))
