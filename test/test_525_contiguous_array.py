from unittest import TestCase
from problems.N525_Contiguous_Array import Solution

class TestSolution(TestCase):
    def test_findMaxLength(self):
        self.assertEqual(2, Solution().findMaxLength([0,1]))

    def test_findMaxLength_1(self):
        self.assertEqual(2, Solution().findMaxLength([0,1,0]))

    def test_findMaxLength_2(self):
        self.assertEqual(2, Solution().findMaxLength([0,1,1]))

    def test_findMaxLength_3(self):
        self.assertEqual(2, Solution().findMaxLength([0,1,1,1,1,1,1,0]))

    def test_findMaxLength_4(self):
        self.assertEqual(4, Solution().findMaxLength([0,1,0,1]))


