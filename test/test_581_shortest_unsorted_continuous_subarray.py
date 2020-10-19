from unittest import TestCase
from problems.N581_Shortest_Unsorted_Continuous_Subarray import Solution

class TestSolution(TestCase):
    def test_findUnsortedSubarray(self):
        self.assertEqual(5, Solution().findUnsortedSubarray([2,6,4,8,10,9,15]))

    def test_findUnsortedSubarray_1(self):
        self.assertEqual(0, Solution().findUnsortedSubarray([1,2,3,4]))

    def test_findUnsortedSubarray_2(self):
        self.assertEqual(0, Solution().findUnsortedSubarray([1]))

    def test_findUnsortedSubarray_3(self):
        self.assertEqual(2, Solution().findUnsortedSubarray([1,3,2,3,3]))

    def test_findUnsortedSubarray_4(self):
        self.assertEqual(4, Solution().findUnsortedSubarray([1,3,5,4,2]))

    def test_findUnsortedSubarray_5(self):
        self.assertEqual(5, Solution().findUnsortedSubarray([2,1,3,5,4]))

    def test_findUnsortedSubarray_6(self):
        self.assertEqual(4, Solution().findUnsortedSubarray([1,3,2,2,2]))

    def test_findUnsortedSubarray_7(self):
        self.assertEqual(4, Solution().findUnsortedSubarray([1,3,5,2,4]))