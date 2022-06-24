from unittest import TestCase
from problems.N689_Maximum_Sum_Of_3_Non_Overlapping_Subarrays import Solution

class TestSolution(TestCase):
    def test_maxSumOfThreeSubarrays(self):
        self.assertListEqual([0, 3, 5], Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))

    def test_maxSumOfThreeSubarrays_1(self):
        self.assertListEqual([1, 4, 7], Solution().maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19], 3))

    def test_maxSumOfThreeSubarrays_2(self):
        self.assertListEqual([4,5,7], Solution().maxSumOfThreeSubarrays([4,5,10,6,11,17,4,11,1,3], 1))

    def test_maxSumOfThreeSubarrays_3(self):
        self.assertListEqual([0,1,2], Solution().maxSumOfThreeSubarrays([4,3,2,1], 1))
