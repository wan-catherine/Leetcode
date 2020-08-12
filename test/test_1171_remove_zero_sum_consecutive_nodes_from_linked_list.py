from unittest import TestCase
from problems.Utility import create_linklist_from_list,create_list_from_linklist
from problems.N1171_Remove_Zero_Sum_Consecutive_Nodes_From_Linked_List import Solution

class TestSolution(TestCase):
    def test_removeZeroSumSublists(self):
        head = create_linklist_from_list([1, 2, -3, 3, 1])
        self.assertListEqual([3,1], create_list_from_linklist(Solution().removeZeroSumSublists(head)))

    def test_removeZeroSumSublists_1(self):
        head = create_linklist_from_list([1,2,3,-3,4])
        self.assertListEqual([1,2,4], create_list_from_linklist(Solution().removeZeroSumSublists(head)))

    def test_removeZeroSumSublists_2(self):
        head = create_linklist_from_list([1,2,3,-3,-2])
        self.assertListEqual([1], create_list_from_linklist(Solution().removeZeroSumSublists(head)))

    def test_removeZeroSumSublists_3(self):
        head = create_linklist_from_list([0,0])
        self.assertListEqual([], create_list_from_linklist(Solution().removeZeroSumSublists(head)))