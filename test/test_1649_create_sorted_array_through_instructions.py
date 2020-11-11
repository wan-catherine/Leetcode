from unittest import TestCase
from problems.N1649_Create_Sorted_Array_Through_Instructions import Solution

class TestSolution(TestCase):
    def test_createSortedArray(self):
        self.assertEqual(1, Solution().createSortedArray([1,5,6,2]))

    def test_createSortedArray_1(self):
        self.assertEqual(3, Solution().createSortedArray([1,2,3,6,5,4]))

    def test_createSortedArray_2(self):
        self.assertEqual(4, Solution().createSortedArray([1,3,3,3,2,4,2,1,2]))
