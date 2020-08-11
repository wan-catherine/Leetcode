from unittest import TestCase
from problems.Utility import create_list_from_linklist,create_linklist_from_list
from problems.N445_Add_Two_Numbers_II import Solution

class TestSolution(TestCase):
    def test_addTwoNumbers(self):
        l1 = create_linklist_from_list([7,2,4,3])
        l2 = create_linklist_from_list([5,6,4])
        self.assertListEqual([7,8,0,7], create_list_from_linklist(Solution().addTwoNumbers(l1, l2)))

    def test_addTwoNumbers_1(self):
        l1 = create_linklist_from_list([0])
        l2 = create_linklist_from_list([0])
        self.assertListEqual([0], create_list_from_linklist(Solution().addTwoNumbers(l1, l2)))
