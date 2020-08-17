from unittest import TestCase
from problems.N1248_Count_Number_Of_Nice_Subarrays import Solution

class TestSolution(TestCase):
    def test_numberOfSubarrays(self):
        self.assertEqual(2, Solution().numberOfSubarrays(nums = [1,1,2,1,1], k = 3))

    def test_numberOfSubarrays_1(self):
        self.assertEqual(0, Solution().numberOfSubarrays(nums = [2,4,6], k = 1))

    def test_numberOfSubarrays_2(self):
        self.assertEqual(16, Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
