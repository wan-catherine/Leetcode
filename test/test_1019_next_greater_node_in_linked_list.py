from unittest import TestCase
from problems.N1019_Next_Greater_Node_In_Linked_List import Solution
from problems.Utility import create_linklist_from_list, create_list_from_linklist

class TestSolution(TestCase):
    def test_nextLargerNodes(self):
        self.assertListEqual([5,5,0], Solution().nextLargerNodes(create_linklist_from_list([2,1,5])))

    def test_nextLargerNodes_1(self):
        self.assertListEqual([7,0,5,5,0], Solution().nextLargerNodes(create_linklist_from_list([2,7,4,3,5])))

    def test_nextLargerNodes_2(self):
        self.assertListEqual([7,9,9,9,0,5,0,0], Solution().nextLargerNodes(create_linklist_from_list([1,7,5,1,9,2,5,1])))
