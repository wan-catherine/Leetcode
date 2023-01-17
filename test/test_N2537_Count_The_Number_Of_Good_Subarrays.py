from unittest import TestCase
from problems.N2537_Count_The_Number_Of_Good_Subarrays import Solution

class TestSolution(TestCase):
    def test_count_good(self):
        self.assertEqual(1, Solution().countGood(nums = [1,1,1,1,1], k = 10))

    def test_count_good_1(self):
        self.assertEqual(4, Solution().countGood(nums = [3,1,4,3,2,2,4], k = 2))