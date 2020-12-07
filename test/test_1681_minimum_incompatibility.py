from unittest import TestCase
from problems.N1681_Minimum_Incompatibility import Solution

class TestSolution(TestCase):
    def test_minimumIncompatibility(self):
        self.assertEqual(4, Solution().minimumIncompatibility(nums = [1,2,1,4], k = 2))

    def test_minimumIncompatibility_1(self):
        self.assertEqual(6, Solution().minimumIncompatibility(nums = [6,3,8,1,3,1,2,2], k = 4))

    def test_minimumIncompatibility_2(self):
        self.assertEqual(-1, Solution().minimumIncompatibility(nums = [5,3,3,6,3,3], k = 3))

    def test_minimumIncompatibility_3(self):
        self.assertEqual(4, Solution().minimumIncompatibility([2,9,4,7,6,8,2,1,10,1,5,4], 2))
