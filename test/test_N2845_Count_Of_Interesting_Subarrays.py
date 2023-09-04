from unittest import TestCase
from problems.N2845_Count_Of_Interesting_Subarrays import Solution

class TestSolution(TestCase):
    def test_count_interesting_subarrays(self):
        self.assertEquals(3, Solution().countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1))

    def test_count_interesting_subarrays_1(self):
        self.assertEquals(2, Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0))

    def test_count_interesting_subarrays_2(self):
        self.assertEquals(1, Solution().countInterestingSubarrays(nums = [7, 2], modulo = 7, k = 0))

    def test_count_interesting_subarrays_3(self):
        self.assertEquals(2, Solution().countInterestingSubarrays(nums = [2,2,5], modulo = 3, k = 2))

    def test_count_interesting_subarrays_4(self):
        self.assertEquals(5, Solution().countInterestingSubarrays(nums = [11,12,21,31], modulo = 10, k = 1))
