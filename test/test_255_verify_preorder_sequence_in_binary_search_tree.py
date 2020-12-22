from unittest import TestCase
from problems.N255_Verify_Preorder_Sequence_In_Binary_Search_Tree import Solution

class TestSolution(TestCase):
    def test_verifyPreorder(self):
        self.assertFalse(Solution().verifyPreorder([5,2,6,1,3]))

    def test_verifyPreorder_1(self):
        self.assertTrue(Solution().verifyPreorder([5,2,1,3,6]))

    def test_verifyPreorder_2(self):
        self.assertTrue(Solution().verifyPreorder([2, 1]))
