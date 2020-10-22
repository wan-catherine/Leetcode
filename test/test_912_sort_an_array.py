from unittest import TestCase
from problems.N912_Sort_An_Array import Solution

class TestSolution(TestCase):
    def test_sortArray(self):
        self.assertListEqual([1,2,3,5], Solution().sortArray([5,2,3,1]))

    def test_sortArray_1(self):
        self.assertListEqual([0,0,1,1,2,5], Solution().sortArray([5,1,1,2,0,0]))
