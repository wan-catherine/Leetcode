from unittest import TestCase
from problems.N1104_Path_In_Zigzag_Labelled_Binary_Tree import Solution

class TestSolution(TestCase):
    def test_pathInZigZagTree(self):
        self.assertListEqual([1,3,4,14], Solution().pathInZigZagTree(14))

    def test_pathInZigZagTree_1(self):
        self.assertListEqual([1,2,6,10,26], Solution().pathInZigZagTree(26))

    def test_pathInZigZagTree_2(self):
        self.assertListEqual([1,3,4,15,16], Solution().pathInZigZagTree(16))
