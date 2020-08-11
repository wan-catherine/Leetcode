from unittest import TestCase
from problems.Utility import create_list_from_linklist, create_linklist_from_list
from problems.N147_Insertion_Sort_List import Solution

class TestSolution(TestCase):
    def test_insertionSortList(self):
        head = create_linklist_from_list([4,2,1,3])
        self.assertListEqual([1,2,3,4], create_list_from_linklist(Solution().insertionSortList(head)))

    def test_insertionSortList_1(self):
        head = create_linklist_from_list([-1,5,3,4,0])
        self.assertListEqual([-1,0,3,4,5], create_list_from_linklist(Solution().insertionSortList(head)))
