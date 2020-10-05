from unittest import TestCase
from problems.N1498_Number_Of_Subsequences_That_Satisfy_The_Given_Sum_Condition import Solution

class TestSolution(TestCase):
    def test_numSubseq(self):
        self.assertEqual(4, Solution().numSubseq(nums = [3,5,6,7], target = 9))

    def test_numSubseq_1(self):
        self.assertEqual(6, Solution().numSubseq(nums = [3,3,6,8], target = 10))

    def test_numSubseq_2(self):
        self.assertEqual(61, Solution().numSubseq(nums = [2,3,3,4,6,7], target = 12))

    def test_numSubseq_3(self):
        self.assertEqual(127, Solution().numSubseq(nums = [5,2,4,1,7,6,8], target = 16))

    def test_numSubseq_4(self):
        self.assertEqual(262119, Solution().numSubseq([11,9,11,13,4,13,9,9,10,1,9,6,5,2,1,8,5,5], 22))
