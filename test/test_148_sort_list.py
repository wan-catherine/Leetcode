from unittest import TestCase
from problems.N148_Sort_List import Solution
from problems.Utility import create_linklist_from_list, create_list_from_linklist

class TestSolution(TestCase):
    def test_sortList(self):
        self.assertListEqual([1,2,3,4], create_list_from_linklist(Solution().sortList(create_linklist_from_list([4,2,1,3]))))

    def test_sortList_1(self):
        li = create_linklist_from_list([-1,5,3,4,0])
        self.assertListEqual([-1,0,3,4,5], create_list_from_linklist(Solution().sortList(li)))
