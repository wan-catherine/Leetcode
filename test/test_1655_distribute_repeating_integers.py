from unittest import TestCase
from problems.N1655_Distribute_Repeating_Integers import Solution

class TestSolution(TestCase):
    def test_canDistribute(self):
        self.assertFalse(Solution().canDistribute(nums = [1,2,3,4], quantity = [2]))

    def test_canDistribute_1(self):
        self.assertTrue(Solution().canDistribute(nums = [1,2,3,3], quantity = [2]))

    def test_canDistribute_2(self):
        self.assertTrue(Solution().canDistribute(nums = [1,1,2,2], quantity = [2,2]))

    def test_canDistribute_3(self):
        self.assertFalse(Solution().canDistribute(nums = [1,1,2,3], quantity = [2,2]))

    def test_canDistribute_4(self):
        self.assertTrue(Solution().canDistribute(nums = [1,1,1,1,1], quantity = [2,3]))

