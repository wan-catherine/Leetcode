from unittest import TestCase
from problems.N1546_Maximum_Number_Of_Non_Overlapping_Subarrays_With_Sum_Equals_Target import Solution

class TestSolution(TestCase):
    def test_maxNonOverlapping(self):
        self.assertEqual(2, Solution().maxNonOverlapping(nums = [1,1,1,1,1], target = 2))

    def test_maxNonOverlapping_1(self):
        self.assertEqual(2, Solution().maxNonOverlapping( nums = [-1,3,5,1,4,2,-9], target = 6))

    def test_maxNonOverlapping_2(self):
        self.assertEqual(3, Solution().maxNonOverlapping(nums = [-2,6,6,3,5,4,1,2,8], target = 10))

    def test_maxNonOverlapping_3(self):
        self.assertEqual(3, Solution().maxNonOverlapping(nums = [0,0,0], target = 0))
