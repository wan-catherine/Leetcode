from unittest import TestCase
from problems.N1755_Closest_Subsequence_Sum import Solution

class TestSolution(TestCase):
    def test_minAbsDifference(self):
        self.assertEqual(0, Solution().minAbsDifference(nums = [5,-7,3,5], goal = 6))

    def test_minAbsDifference_1(self):
        self.assertEqual(1, Solution().minAbsDifference(nums = [7,-9,15,-2], goal = -5))

    def test_minAbsDifference_2(self):
        self.assertEqual(7, Solution().minAbsDifference(nums = [1,2,3], goal = -7))

    def test_minAbsDifference_3(self):
        self.assertEqual(22394, Solution().minAbsDifference([-6651,401,-8998,-9269,-9167,7741,-9699], 30536))

    def test_minAbsDifference_4(self):
        self.assertEqual(10327, Solution().minAbsDifference([1556913,-259675,-7667451,-4380629,-4643857,-1436369,7695949,-4357992,-842512,-118463], -9681425))

    def test_minAbsDifference_5(self):
        self.assertEqual(236, Solution().minAbsDifference([-4816,3637,8511,-1731,-5728,-9723,8373,-8758], 12826))

    def test_minAbsDifference_6(self):
        self.assertEqual(8405, Solution().minAbsDifference([9152249,8464156,-2493402,8990685,-7257152,-1050240,2243737,-82901,8939692], 26915229))