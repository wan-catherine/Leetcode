from unittest import TestCase
from problems.N1574_Shortest_Subarray_To_Be_Removed_To_Make_Array_Sorted import Solution

class TestSolution(TestCase):
    def test_findLengthOfShortestSubarray(self):
        self.assertEqual(3, Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))

    def test_findLengthOfShortestSubarray_1(self):
        self.assertEqual(4, Solution().findLengthOfShortestSubarray([5,4,3,2,1]))

    def test_findLengthOfShortestSubarray_2(self):
        self.assertEqual(0, Solution().findLengthOfShortestSubarray([1,2,3]))

    def test_findLengthOfShortestSubarray_3(self):
        self.assertEqual(0, Solution().findLengthOfShortestSubarray([1]))

    def test_findLengthOfShortestSubarray_4(self):
        self.assertEqual(8, Solution().findLengthOfShortestSubarray([13,0,14,7,18,18,18,16,8,15,20]))


