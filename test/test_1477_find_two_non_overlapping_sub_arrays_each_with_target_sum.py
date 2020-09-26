from unittest import TestCase
from problems.N1477_Find_Two_Non_Overlapping_Sub_Arrays_Each_With_Target_Sum import Solution

class TestSolution(TestCase):
    def test_minSumOfLengths(self):
        self.assertEqual(2, Solution().minSumOfLengths(arr = [3,2,2,4,3], target = 3))

    def test_minSumOfLengths_1(self):
        self.assertEqual(2, Solution().minSumOfLengths(arr = [7,3,4,7], target = 7))

    def test_minSumOfLengths_2(self):
        self.assertEqual(-1, Solution().minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6))

    def test_minSumOfLengths_3(self):
        self.assertEqual(-1, Solution().minSumOfLengths(arr = [5,5,4,4,5], target = 3))

    def test_minSumOfLengths_4(self):
        self.assertEqual(3, Solution().minSumOfLengths(arr = [3,1,1,1,5,1,2,1], target = 3))

