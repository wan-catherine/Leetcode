from unittest import TestCase
from problems.N3176_Find_The_Maximum_Length_Of_A_Good_Subsequence_I import Solution

class TestSolution(TestCase):
    def test_maximum_length(self):
        self.assertEquals(4, Solution().maximumLength(nums = [1,2,1,1,3], k = 2))

    def test_maximum_length_1(self):
        self.assertEquals(2, Solution().maximumLength(nums = [1,2,3,4,5,1], k = 0))

    def test_maximum_length_2(self):
        self.assertEquals(2, Solution().maximumLength(nums = [30,30,29], k = 0))
