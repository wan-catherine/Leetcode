from unittest import TestCase
from problems.N328_Odd_Even_Linked_List import Solution
from problems.Utility import create_linklist_from_list,create_list_from_linklist

class TestSolution(TestCase):
    def test_oddEvenList(self):
        head = create_linklist_from_list([1,2,3,4,5])
        result = create_list_from_linklist(Solution().oddEvenList(head))
        self.assertListEqual([1,3,5,2,4], result)

    def test_oddEvenList_1(self):
        head = create_linklist_from_list([2,1,3,5,6,4,7])
        result = create_list_from_linklist(Solution().oddEvenList(head))
        self.assertListEqual([2,3,6,7,1,5,4], result)

    def test_oddEvenList_2(self):
        head = create_linklist_from_list([1,2,3,4,5,6,7,8])
        result = create_list_from_linklist(Solution().oddEvenList(head))
        self.assertListEqual([1,3,5,7,2,4,6,8], result)
