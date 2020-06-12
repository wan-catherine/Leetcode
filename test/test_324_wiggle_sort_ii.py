from unittest import TestCase
from problems.N324_Wiggle_Sort_II import Solution

class TestSolution(TestCase):
    def test_wiggleSort(self):
        self.assertListEqual([1, 6, 1, 5, 1, 4], Solution().wiggleSort([1, 5, 1, 1, 6, 4]))

    def test_wiggleSort_1(self):
        self.assertListEqual([2, 3, 1, 3, 1, 2], Solution().wiggleSort([1, 3, 2, 2, 3, 1]))

    def test_wiggleSort_2(self):
        self.assertListEqual([1,2,1,2,1,2,1], Solution().wiggleSort([1,1,2,1,2,2,1]))

    def test_wiggleSort_3(self):
        self.assertListEqual([1,2,1,2,1,2,1], Solution().wiggleSort([1,2,2,1,2,1,1,1,1,2,2,2]))