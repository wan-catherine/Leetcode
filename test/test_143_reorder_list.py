from unittest import TestCase
from problems.N143_Reorder_List import Solution
from problems.Utility import create_linklist_from_list, create_list_from_linklist

class TestSolution(TestCase):
    def test_reorderList(self):
        head = create_linklist_from_list([1,2,3,4])
        Solution().reorderList(head)
        self.assertListEqual([1,4,2,3],create_list_from_linklist(head))

    def test_reorderList_1(self):
        head = create_linklist_from_list([1,2,3,4,5])
        Solution().reorderList(head)
        self.assertListEqual([1,5,2,4,3],create_list_from_linklist(head))