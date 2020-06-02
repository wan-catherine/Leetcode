from unittest import TestCase
from problems.N718_Maximum_Length_Of_Repeated_Subarray import Solution

class TestSolution(TestCase):
    def test_findLength(self):
        self.assertEqual(3, Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))

    def test_findLength_1(self):
        self.assertEqual(2, Solution().findLength([0,1,1,1,1],[1,0,1,0,1]))

    def test_findLength_2(self):
        self.assertEqual(3, Solution().findLength([1,0,0,0,1],[1,0,0,1,1]))
