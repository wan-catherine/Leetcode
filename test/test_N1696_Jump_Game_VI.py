from unittest import TestCase
from problems.N1696_Jump_Game_VI import Solution

class TestSolution(TestCase):
    def test_max_result(self):
        self.assertEqual(7, Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2))

    def test_max_result_1(self):
        self.assertEqual(17, Solution().maxResult(nums = [10,-5,-2,4,0,3], k = 3))

    def test_max_result_2(self):
        self.assertEqual(0, Solution().maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))