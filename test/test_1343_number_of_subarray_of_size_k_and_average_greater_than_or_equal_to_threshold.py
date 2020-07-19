from unittest import TestCase
from problems.N1343_Number_Of_Subarray_Of_Size_K_And_Average_Greater_Than_Or_Equal_To_Threshold import Solution

class TestSolution(TestCase):
    def test_numOfSubarrays(self):
        self.assertEqual(3, Solution().numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))

    def test_numOfSubarrays_1(self):
        self.assertEqual(5, Solution().numOfSubarrays( arr = [1,1,1,1,1], k = 1, threshold = 0))

    def test_numOfSubarrays_2(self):
        self.assertEqual(6, Solution().numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))

    def test_numOfSubarrays_3(self):
        self.assertEqual(1, Solution().numOfSubarrays(arr = [7,7,7,7,7,7,7], k = 7, threshold = 7))

    def test_numOfSubarrays_4(self):
        self.assertEqual(1, Solution().numOfSubarrays(arr = [4,4,4,4], k = 4, threshold = 1))

